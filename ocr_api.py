import os
import cv2
import requests
import json
import config


# Text extraction performed here
# Convert to base64
# Set up payload using documentation parameters
# Send request to API
# Parse JSON response from API
# Extract text from JSON response

def api_extraction(image):

    # endpoint URL
    api_url = "https://api.ocr.space/parse/image"

    # need to encode image as Base64 for OCR
    _, image_data = cv2.imencode(".jpg", image)
    image_base64 = image_data.tobytes()

    # set request parameters
    payload = {
        "apikey": config.API_KEY,
        "base64image": image_base64,
        "language": "jpn",
        "OCREngine": "2",
    }

    # make request to API
    # 10 seconds may be too short 
    try:
        response = requests.post(api_url, data=payload, timeout=30)
        response.raise_for_status()  
        ocr_response = response.json()

    
        if "ParsedResults" in ocr_response and ocr_response["ParsedResults"]:
            extracted_text = ocr_response["ParsedResults"][0]["ParsedText"]
            return extracted_text
        else:
            print("OCR API response does not contain any text.")
            return None

    except requests.exceptions.ReadTimeout:
        print("API request timed out. Please try again later.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the API request: {e}")
        return None

    

    # return extracted_text