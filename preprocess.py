import cv2
import os

# Many ways to preprocess images for extraction and translation
# I am not sure which methods will need to be used yet


# Grayscale conversion
def preprocess_image(image):
    gray_preprocess = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_preprocess