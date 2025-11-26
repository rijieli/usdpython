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

`usdzconvert` is a Python script that converts various 3D file formats to USDZ.
It also performs asset validation on the generated usdz.
For more information, run 

    usdzconvert -h

### Supported Input Formats

| Format | Extension | Type | Description |
| ------ | --------- | ---- | ----------- |
| OBJ | `.obj` | Multi-file | Wavefront OBJ with `.mtl` and textures (folder input auto-enables MTL) |
| glTF | `.gltf` | Multi-file | GL Transmission Format (text) with `.bin` data and textures |
| GLB | `.glb` | Single file | GL Transmission Format (binary, all assets embedded) |
| FBX | `.fbx` | Single file | Autodesk FBX (requires FBX SDK, see below) |
| Alembic | `.abc` | Single file | Alembic interchange format |
| USD | `.usd`, `.usda`, `.usdc` | Multi-file | Universal Scene Description (may reference textures) |
| USDZ | `.usdz` | Single file | Compressed USD package (all assets bundled) |

> **Note:** USDZ → USDZ conversion is useful for modifying metadata (`-url`, `-creator`, `-copyright`), adjusting scale (`-metersPerUnit`), changing animation loop settings (`-loop`/`-no-loop`), or applying iOS 12 compatibility (`-iOS12`).

### Usage

Run with `uv`:
```bash
./usdzconvert [options] inputFile [outputFile]
# or directly:
uv run src/usdzconvert.py [options] inputFile [outputFile]
```

OBJ files support both file and folder input:
```bash
./usdzconvert model.obj -useObjMtl      # File input with MTL materials
./usdzconvert model_folder/             # Folder input (auto-enables -useObjMtl)
```

Output file handling:
```bash
./usdzconvert model.obj                 # Output: model.usdz (same folder)
./usdzconvert model.obj output          # Output: output.usdz (auto-adds .usdz)
./usdzconvert model.obj output.usdz     # Output: output.usdz (in source folder)
./usdzconvert input.usdz                # Output: input_converted.usdz (adds suffix)
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


