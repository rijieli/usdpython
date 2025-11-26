#!/bin/bash

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Change to the script directory (project root)
cd "$SCRIPT_DIR"

# Run usdzconvert.py using uv
uv run usdzconvert/usdzconvert.py "$@"

