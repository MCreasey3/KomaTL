import os 
import cv2

from load_image import load_image
from preprocess import preprocess_image


# load image for preprocessing -> text extraction -> translation
image_path = "inputImages/input.jpg"
image = load_image(image_path)

preprocessed_image = preprocess_image(image)

# Establish output directory
output_path = "OutputImages/grayscale.jpg"

# Save grayscaled image
cv2.imwrite(output_path, preprocessed_image)
print("Grayscaled image saved, please verify.")