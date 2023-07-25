import os 
import cv2
import config


from load_image import load_image
from preprocess import preprocess_image
from ocr_api import api_extraction


# load image for preprocessing -> text extraction -> translation
image_path = "inputImages/input.jpg"
image = load_image(image_path)

preprocessed_image = preprocess_image(image)

# Establish output directory
# For now, this will be used to verify preprocessing.
output_path = "OutputImages/preprocessed.jpg"

# Save preprocessed image
# Saved for testing
# cv2.imwrite(output_path, preprocessed_image)
# print("Binary image saved, please verify.")

# Call API and save extracted JPN text
extracted_text = api_extraction(preprocessed_image)

# print for OCR verify test
print(extracted_text)