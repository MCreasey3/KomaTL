import cv2
# import os
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
    # return binary_preprocess

    # Skew Correction
    coordinates = numpy.column_stack(numpy.where(binary_preprocess > 0))
    angle = cv2.minAreaRect(coordinates)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle

    # Check for > 3 degrees skew to correct
    angle_max = 5
    if abs(angle) < angle_max:
        return binary_preprocess # Skip correction when unnecessary
    
    # No skip
    (height, width) = binary_preprocess.shape[:2]
    center = (width // 2, height // 2)
    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    skewcorrected_image = cv2.warpAffine(binary_preprocess, matrix, (width, height), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    # return skewcorrected_image


    # Noise reduction via mathematical morphology
    kernel = numpy.ones((3, 3), numpy.uint8)
    denoised_image = cv2.morphologyEx(skewcorrected_image, cv2.MORPH_OPEN, kernel)
    return denoised_image