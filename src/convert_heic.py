import os
from pillow_heif import register_heif_opener
from PIL import Image

# Register the HEIF opener
register_heif_opener()


def convert_heic_to_jpeg(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".heic"):
            input_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + ".jpg"
            output_path = os.path.join(output_folder, output_filename)

            try:
                # Open the HEIC image
                with Image.open(input_path) as img:
                    # Convert and save as JPEG
                    img.convert("RGB").save(output_path, "JPEG")
                print(f"Converted {filename} to {output_filename}")
            except Exception as e:
                print(f"Error converting {filename}: {str(e)}")


# Usage
input_folder = "/Users/survy/Downloads/cones"
output_folder = "/Users/survy/Downloads/cones_jpg"

convert_heic_to_jpeg(input_folder, output_folder)
