import os
import sys
from PIL import Image

try:
    import pillow_heif
    pillow_heif.register_heif_opener()
except ImportError:
    pillow_heif = None

def convert_heic_to_jpg(input_path, output_path=None):
    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + ".jpg"
    
    try:
        with Image.open(input_path) as img:
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.save(output_path, 'JPEG', quality=95)
        
        print(f"Converted: {input_path} -> {output_path}")
        return output_path
    except Exception as e:
        if "cannot identify image file" in str(e):
            print(f"Error: HEIC format not supported. Install pillow-heif:")
            print("  pip install pillow-heif")
        else:
            print(f"Error converting {input_path}: {e}")
        return None

def convert_folder(folder_path):
    heic_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.heic')]
    
    if not heic_files:
        print("No HEIC files found.")
        return
    
    for filename in heic_files:
        input_path = os.path.join(folder_path, filename)
        convert_heic_to_jpg(input_path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python heic_to_jpg.py <file.heic>")
        print("       python heic_to_jpg.py <folder>")
    else:
        path = sys.argv[1]
        if os.path.isfile(path):
            convert_heic_to_jpg(path)
        elif os.path.isdir(path):
            convert_folder(path)