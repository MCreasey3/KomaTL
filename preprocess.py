import cv2
import os
import numpy

# We begin with converting the image to grayscale, and then performing Otsu's Binarization
# Later, we will do a skew correction and follow up with noise removal to prepare for OCR. 


# Image preprocessing steps
def preprocess_image(image):
    # Grayscale conversion
    gray_preprocess = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # return gray_preprocess
    
    # Otsu's Binarization
    _, binary_preprocess = cv2.threshold(gray_preprocess, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    return binary_preprocess