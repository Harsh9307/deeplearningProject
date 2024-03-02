import os
from PIL import ImageEnhance,Image

ORIGIN_PATH = r"C:\Users\diwas\Desktop\deeplearningProject\dataset\adenocarcinoma"
DESTIN_PATH = r"C:\Users\diwas\Desktop\deeplearningProject\preprocessing\preprocessed_dataset\adenocarcinoma"

# Create destination directory if it doesn't exist
if not os.path.exists(DESTIN_PATH):
    os.makedirs(DESTIN_PATH)

# Loop through all files in the origin directory
for filename in os.listdir(ORIGIN_PATH):
    # Construct full paths for the original and destination images
    origin_image_path = os.path.join(ORIGIN_PATH, filename)
    destin_image_path = os.path.join(DESTIN_PATH, filename)
    
    # Open the image file
    with Image.open(origin_image_path) as img:
        # Resize the image
        out = img.resize((300, 300))
        # Save the converted image to the destination directory
        out.save(destin_image_path, format="PNG")