# README

## Overview

This repository contains two Python scripts:

1. **`splitsvg.py`**: Extracts all groups and paths from an SVG file and saves them as separate SVG files.
2. **`install.py`**: Installs a context menu entry in Windows for splitting SVG files using the `splitsvg.py` script.

## Requirements

- Python 3.x
- `WindowsContextMenu` package (required for `install.py`)

## Usage

### `splitsvg.py`

This script processes an SVG file to extract all groups and paths, saving them as individual SVG files.

#### How to Use

1. Run the script from the command line:
    ```bash
    python extract_paths.py <path_to_svg_file>
    ```
2. The script will create a directory named `exported_paths` in the same location as the input SVG file. Each group of paths will be saved as a separate SVG file in this directory.

### `install.py`

This script installs a context menu entry in Windows that allows you to right-click on an SVG file and split it using the `splitsvg.py` script.

#### How to Use

1. Ensure you have the `WindowsContextMenu` package installed. If not, you can install it by running the following commands:
    ```bash
    git clone https://github.com/offerrall/WindowsContextMenu
    cd WindowsContextMenu
    pip install .
    ```

2. Run the `install.py` script as an administrator:
    ```bash
    python install.py
    ```
3. After installation, you can right-click on any `.svg` file in Windows Explorer and select "Split SVG" from the context menu to run the script.

## Troubleshooting

- If you receive an error about needing to run as administrator, ensure that you are running the `install.py` script with administrator privileges.
- If the `WindowsContextMenu` package is not found, follow the installation steps in the **Usage** section.

## License

This project is licensed under the MIT License.
