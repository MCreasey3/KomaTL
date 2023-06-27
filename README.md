# KomaTL

<h3>🔹 Context-aware translator designed for web comics 🔹</h3>

KomaTL is an intelligent translator program designed for translating text on images into another language. For this project, we will be focusing on translating Japanese text into English, and performing a simple text replacement on the finalized output image.

<hr>
This program leverages several open-source libraries across the translation process. Preprocessing is handled by the OpenCV-Python library to prepare the image for text extraction. Extraction is done using the Tesseract OCR engine. Translation is performed with the DeepL Translate API. OpenCV-Python (CV2) is also utilized in post-translation to replace the old text, and render the new text onto the image. 
<hr>
Images will initially be stored in the 'InputImages' directory, and must be named input.jpg. This will be expanded in the future to allow for automatic file renaming and support for the .png extension as well. Completed files will appear in the 'OutputImages' directory. 
<hr>

As always, you can install the required packages using `pip install -r requirements.txt` in a virtual environment. You can run the program with a simple `python3 main.py`.

<hr>

:star: 4-STEP PREPROCESSING :star:

To better optimize the OCR phase, we first convert the image to grayscale and perform Otsu's Binarization, which computes a threshold white/black value across the entirety of the image. We follow this by performing a check for a rotational skew greater than 3 degrees, and fix as necessary. This will improve performance of the OCR engine. We finish by applying noise reduction to the image.

NOTE on noise reduction: Typically this is done to grayscale or color images, but for binary images, we can use OpenCV's morphological operations to attack very small regions or thin lines in the image. This can mess with detail if done incorrectly, so it will be set fairly conservatively.

<hr>

:large_blue_diamond: OPTICAL CHARACTER RECOGNITION :large_blue_diamond:

My OCR engine of choice for this project is Tesseract OCR, developed by Google. Traditionally, Tesseract is used with its standard C and C++ APIs. However, KomaTL utilizes `pytesseract`, a Python wrapper for Tesseract. 
