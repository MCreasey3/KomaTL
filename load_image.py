import os
import cv2

# load image file for preprocessing -> extraction -> translation -> postprocessing
def load_image(image_path):
    image = cv2.imread(image_path)
    return image