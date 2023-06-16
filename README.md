# KomaTL
<h3 style="text-align: center;">Context-aware translator designed for web comics</h3>

KomaTL is an intelligent translator program designed for translating text on images into another language. For this project, we will be focusing on translating Japanese text into English, and performing a simple text replacement on the finalized output image. 
<hr>
This program leverages several open-source libraries across the translation process. Preprocessing is handled by the OpenCV-Python library to prepare the image for text extraction. Extraction is done using the Tesseract OCR. Translation is performed with the DeepL Translate API. OpenCV-Python (CV2) is also utilized in post-translation to replace the old text, and render the new text onto the image. 
<hr>
Images will initially be stored in the 'InputImages' directory, and must be named input.jpg. This will be expanded in the future to allow for automatic file renaming and support for the .png extension as well. Completed files will appear in the 'OutputImages' directory. 
<hr>

As always, you can install the required packages using `pip install -r requirements.txt` in a virtual environment. You can run the program with a simple `python3 main.py`. 
