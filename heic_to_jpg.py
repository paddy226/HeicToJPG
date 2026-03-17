import os
import sys
import argparse
from PIL import Image

try:
    import pillow_heif
    pillow_heif.register_heif_opener()
except ImportError:
    pillow_heif = None

def convert_heic_to_jpg(input_path, output_path=None, quality=95):
    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + ".jpg"
    
    try:
        with Image.open(input_path) as img:
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.save(output_path, 'JPEG', quality=quality)
        
        print(f"Converted: {input_path} -> {output_path}")
        return output_path
    except Exception as e:
        if "cannot identify image file" in str(e):
            print(f"Error: HEIC format not supported. Install pillow-heif:")
            print("  pip install pillow-heif")
        else:
            print(f"Error converting {input_path}: {e}")
        return None

def convert_folder(folder_path, quality=95):
    heic_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.heic')]
    
    if not heic_files:
        print("No HEIC files found.")
        return
    
    for filename in heic_files:
        input_path = os.path.join(folder_path, filename)
        convert_heic_to_jpg(input_path, quality=quality)

VERSION = "1.0.0"

def main():
    parser = argparse.ArgumentParser(
        description="Convert HEIC images to JPG format."
    )
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {VERSION}")
    parser.add_argument("path", help="HEIC file or folder containing HEIC files")
    parser.add_argument("-q", "--quality", type=int, default=95, help="JPG quality (1-100, default: 95)")
    
    args = parser.parse_args()
    path = args.path
    
    if os.path.isfile(path):
        convert_heic_to_jpg(path, quality=args.quality)
    elif os.path.isdir(path):
        convert_folder(path, quality=args.quality)
    else:
        print(f"Error: Path not found: {path}")

if __name__ == "__main__":
    main()