# HEIC to JPG Converter

Convert HEIC images to JPG format.

## Install

```bash
pip install -r requirements.txt
```

## Usage

```bash
# Convert single file
python heic_to_jpg.py <file.heic>

# Convert all HEIC in folder
python heic_to_jpg.py <folder>
```

## Options

- `-h, --help` - Show help message
- `-v, --version` - Show version
- `-q, --quality` - JPG quality (1-100, default: 95)

## Build EXE

```bash
pip install pyinstaller
python -m PyInstaller --onefile heic_to_jpg.py
```

Output: `dist/heic_to_jpg.exe`