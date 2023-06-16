import os 
import cv2

from load_image import load_image
from preprocess import preprocess_image


# load image for preprocessing -> text extraction -> translation
image_path = "inputImages/input.jpg"
image = load_image(image_path)

preprocessed_image = preprocess_image(image)

# Establish output directory
# For now, this will be used to verify preprocessing.
output_path = "OutputImages/preprocessed.jpg"

# Save grayscaled image
cv2.imwrite(output_path, preprocessed_image)
print("Binary image saved, please verify.")