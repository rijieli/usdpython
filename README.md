# USD Python Tools

**⚠️ This project requires [uv](https://github.com/astral-sh/uv) to run.** Install uv first, then all dependencies will be automatically managed.

This package contains:
- `usdzconvert` - converts from various file formats to usdz (use `./usdzconvert`)
- `usdARKitChecker` - validates usdz files (use `./usdARKitChecker`)
- Sample scripts - demonstrate how to write usd files (in `samples/` directory)
- `fixOpacity` - fixes translucent materials (use `./fixOpacity`)
- `usdzcreateassetlib` - generates asset library from multiple usdz assets (use `./usdzcreateassetlib`)
- `usdzaudioimport` - attaches audio files to usdz files (use `./usdzaudioimport`)

**Requirements:**
- [uv](https://github.com/astral-sh/uv) package manager
- Python 3.8 (automatically managed by uv)

For more details, including demos, see the WWDC 2019 session "Working with USD": 
https://developer.apple.com/videos/play/wwdc2019/602/

## usdzconvert (version 0.66)

`usdzconvert` is a Python script that converts obj, gltf, fbx, abc, and usda/usdc/usd assets to usdz.
It also performs asset validation on the generated usdz.
For more information, run 

    usdzconvert -h

### Usage

Run with `uv`:
```bash
./usdzconvert [options] inputFile [outputFile]
# or directly:
uv run src/usdzconvert.py [options] inputFile [outputFile]
```

OBJ files support both file and folder input:
```bash
./usdzconvert model.obj -useObjMtl          # File input
./usdzconvert model_folder/ -useObjMtl     # Folder input (auto-finds .obj, .mtl, textures)
```

### iOS 12 Compatibility

Use `-iOS12` flag for iOS 12 compatibility.

### FBX Support

Requires Autodesk FBX SDK. Set `PYTHONPATH` environment variable before running to include FBX Python bindings path (for Python 3.8).

## usdARKitChecker

Validates usdz files. Automatically run by `usdzconvert`, or use standalone:

```bash
./usdARKitChecker [options] file.usdz
```

## USD Library

USD library is provided via the `usd-core` package dependency, automatically installed and managed by `uv`. No manual environment variable setup is required.

## Samples

Example scripts demonstrating USD features (geometry, materials, animation, etc.).

| Script | Purpose |
| ------ | --- |
| `101_scenegraph.py` | creates a scene graph |
| `102_mesh.py` | creates a cube mesh |
| `103_simpleMaterial.py` | creates a simple PBR material |
| `104_texturedMaterial.py` | creates a cube mesh and assigns it a PBR material with a diffuse texture |
| `105_pbrMaterial.py` | creates a cube mesh and assigns it a more complex PBR material with textures for normal, roughness and diffuse channels |
| `106_meshGroups.py` | creates a cube mesh with two mesh groups and assigns each a separate material |
| `107_transformAnimation.py` |  builds a scene graph of several objects and sets (animated) translate, rotate, and scale transforms |
| `108_skinnedAnimation.py` | creates an animated skinned cube |
| `201_subdivision.py` | creates a subdivided cube with creases |
| `202_references.py` | creates an asset file then a reference file that reference and overwrite the asset file|

## fixOpacity

Fixes translucent materials that render opaque in iOS 13:

```bash
./fixOpacity model.usdz
```

## usdzcreateassetlib

Generates a single-file asset library from multiple usdz assets (nested usdz with variant sets):

```bash
./usdzcreateassetlib outputFile.usdz asset1.usdz [asset2.usdz [...]]
```

## usdzaudioimport

Attaches audio files to usdz files with SpatialAudio nodes:

```bash
./usdzaudioimport inputFile.usdz [outputFile] [options]
```


