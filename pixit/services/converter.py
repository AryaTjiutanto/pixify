from PIL import Image
from pixit.helpers.file import get_output_path
from pixit.helpers.Option import parse_size
from typing import Optional
from yaspin import yaspin
import os

IMG_EXTS = (
    '.jpg', '.jpeg', 
    '.png',
    '.webp',
    '.bmp',
    '.tiff', '.tif', 
    '.gif'           
)

def convert_image(input_path:str, output_format:str, output_name:str = None, size:str = None, output_folder:str = None):
    try:
        with yaspin(text="Converting...", color="cyan") as spinner:
            # get the output path
            img = Image.open(input_path)
            output_path = get_output_path(input_path, output_format, output_name, output_folder)

            # save image
            if size or output_format.lower == 'ico':
                if not size:
                    img_size = parse_size("64x64")
                else:
                    img_size = parse_size(size)
                    
                img_resize = img.resize(img_size, Image.Resampling.LANCZOS)
                img_resize.save(output_path, format=output_format.upper())
            else:
                img.save(output_path, output_format.upper())
            
            spinner.ok("✅ ")
            print(f"Converted: {output_path}")
    except FileNotFoundError:
        print("❌ Error: File not found. Please check the input path.")
    except OSError:
        print("❌ Error: Unsupported or corrupted image file.")
    except Exception:
        print("❌ Error: An unexpected error occurred during conversion.")
    
def convert_all_image_in_folder(input_folder:str = None, output_format:str = None, format_filter:str = None, size:str = None, output_folder:str = None):
    folder = input_folder or os.getcwd()

    if not os.path.exists(folder) or not os.path.isdir(folder):
        print(f"❌ Error: Folder '{folder}' does not exist or is not a directory")
        return

    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)

        if not os.path.isfile(filepath):
            continue

        if format_filter:
            if not filepath.lower().endswith(format_filter):
                continue
        else:
            if not filepath.lower().endswith(IMG_EXTS):
                continue

        try:
            convert_image(filepath, output_format, None, size, output_folder)
        except Exception:
            print(f"❌ Failed to convert: {filename}")
