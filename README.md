# USD Python Tools

This package installs to /Applications/usdpython and contains
- `usdzconvert`, a Python-based tool to convert from various file formats to usdz
- `usdARKitChecker`, a Python-based tool for usdz validation
- precompiled macOS Python modules for Pixar's USD library
- a set of sample scripts that demonstrate how to write usd files
- the `fixOpacity` tool
- `usdzcreateassetlib`, a standalone tool to generate an asset library from multiple assets
- `usdzaudioimport`, a standalone tool to attach audio files to usdz files

After installation you can relocate the files.

IMPORTANT! This version of USD Python tools uses Python 3.8. You can download and install Python 3.8 (recommended) from https://www.python.org/downloads/release/python-380/.

The easiest way to start using these command-line tools is to double-click `USD.command` in the Finder. This will open a Terminal window with all necessary environment variables set.

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
./usdzconvert.sh [options] inputFile [outputFile]
```

OBJ files support both file and folder input:
```bash
usdzconvert model.obj -useObjMtl          # File input
usdzconvert model_folder/ -useObjMtl     # Folder input (auto-finds .obj, .mtl, textures)
```

### iOS 12 Compatibility

Use `-iOS12` flag for iOS 12 compatibility.

### FBX Support

Requires Autodesk FBX SDK. Update `USD.command` to include FBX Python bindings path (for Python 3.8).

## usdARKitChecker

Validates usdz files. Automatically run by `usdzconvert`, or use standalone: `usdARKitChecker -h`

## USD Library (Version 19.11)

Compiled with Python 3.8 using USD 22.03. Set environment variables:

    export PATH=$PATH:<PATH_TO_USDPYTHON>/USD
    export PYTHONPATH=$PYTHONPATH:<PATH_TO_USDPYTHON>/USD/lib/python

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

Fixes translucent materials that render opaque in iOS 13: `fixOpacity model.usdz`

## usdzcreateassetlib

Generates a single-file asset library from multiple usdz assets (nested usdz with variant sets).

## usdzaudioimport

Attaches audio files to usdz files with SpatialAudio nodes: `usdzaudioimport -h`


