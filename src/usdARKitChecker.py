

import subprocess, sys, os, argparse
from pxr import *
from validateMesh import validateMesh
from validateMaterial import validateMaterial


def _checkShaderDefsAvailable():
    """Check if USD shader definitions are available in the installation."""
    try:
        registry = Sdr.Registry()
        shader = registry.GetShaderNodeByIdentifier('UsdPreviewSurface')
        return shader is not None
    except:
        return False


# Check once at module load time
_shaderDefsAvailable = _checkShaderDefsAvailable()


def validateFile(file, verbose, errorData):
    stage = Usd.Stage.Open(file)
    success = True
    predicate = Usd.TraverseInstanceProxies(Usd.PrimIsActive & Usd.PrimIsDefined & ~Usd.PrimIsAbstract)
    for prim in stage.Traverse(predicate):
        if prim.GetTypeName() == "Mesh":
            success = validateMesh(prim, verbose, errorData) and success
        if prim.GetTypeName() == "Material":
            success = validateMaterial(prim, verbose, errorData) and success
    return success

def runValidators(filename, verboseOutput, errorData):
    checker = UsdUtils.ComplianceChecker(arkit=True, 
            skipARKitRootLayerCheck=False, rootPackageOnly=False, 
            skipVariants=False, verbose=False)

    checker.CheckCompliance(filename)
    errors = checker.GetErrors()
    failedChecks = checker.GetFailedChecks()
    
    # Track skipped checks due to missing shader definitions
    skippedShaderCheck = False
    
    for rule in checker._rules:
        error = rule.__class__.__name__
        failures = rule.GetFailedChecks()
        if len(failures) > 0:
            # Skip ShaderPropertyTypeConformanceChecker if shader definitions are not available
            # This is a known limitation of the usd-core pip package
            if error == 'ShaderPropertyTypeConformanceChecker' and not _shaderDefsAvailable:
                skippedShaderCheck = True
                continue
            errorData.append({ "code": "PXR_" + error, "failures": failures })
            errors.append(error)

    # Filter out ShaderPropertyTypeConformanceChecker from failedChecks if skipped
    if skippedShaderCheck:
        failedChecks = [fc for fc in failedChecks if 'ShaderPropertyTypeConformanceChecker' not in fc]

    usdCheckerResult = len(errors) == 0
    mdlValidation = validateFile(filename, verboseOutput, errorData)

    success = usdCheckerResult and mdlValidation
    print("usdARKitChecker: " + ("[Pass]" if success else "[Fail]") + " " + filename)
    
    # Print warning about skipped shader check
    if skippedShaderCheck:
        print("  Warning: ShaderPropertyTypeConformanceChecker skipped (usd-core missing shaderDefs.usda)")
    
    # Print failure reasons when check fails
    if not success:
        if len(errors) > 0:
            print("  Compliance errors:")
            for error in errors:
                print(f"    - {error}")
        if len(failedChecks) > 0:
            print("  Failed checks:")
            for check in failedChecks:
                print(f"    - {check}")
        # Print custom validation errors from errorData
        for err in errorData:
            if 'code' in err and not err['code'].startswith('PXR_'):
                details = ', '.join(f"{k}: {v}" for k, v in err.items() if k != 'code')
                print(f"    - {err['code']}: {details}" if details else f"    - {err['code']}")

def main(argumentList, outErrorList=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", "-v", action='store_true', help="Verbose mode.")
    parser.add_argument('files', nargs='*')
    args=parser.parse_args(argumentList)

    verboseOutput = args.verbose
    totalSuccess = True
    for filename in args.files:
        errorData = []
        runValidators(filename, verboseOutput, errorData)
        if outErrorList is not None:
        	outErrorList.append({ "file": filename, "errors": errorData })
        totalSuccess = totalSuccess and len(errorData) == 0

    if totalSuccess:
        return 0
    else:
        return 1

if __name__ == '__main__':
    argumentList = sys.argv[1:]
    sys.exit(main(argumentList))
