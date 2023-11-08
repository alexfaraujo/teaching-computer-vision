import cv2
import pytesseract
from deep_translator import GoogleTranslator, single_detection
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import numpy as np

def read_text(image_path):
    # read the image file
    img_cv = cv2.imread(image_path)
    img_cv = image_resize(img_cv)

    # By default the OpenCV Lib read the image using BGR color map.
    # The pytesseract Lib receives a RGB image as input.
    # So it is necessary convert BGR to RGB
    img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)

    # Extract the text using the function from PyTesseract Lib
    text = pytesseract.image_to_string(img_rgb)

    # Replace "\n" by " " char
    text = text.replace("\n", " ")

    # Ignore small texts
    if not text or len(text) < 20:
        return '{"msg": "error"}'
    else:  # Some text was found

        # Read the language used in the text
        # '02c3e6b8bf0ac88724d7685a28a9eb00' e the Key to access the API of deep_translator
        lang = single_detection(text, '02c3e6b8bf0ac88724d7685a28a9eb00')

        # If the texto is in another language, translate it to Englihs using Google Translator
        if lang != 'en':
            my_translator = GoogleTranslator(source='auto', target='en')
            text = my_translator.translate(text)

    return '{"msg": "'+text+'"}'


def image_resize(image):
    scale_percent = 360/min(image.shape[1], image.shape[0]) # percent of original size
    width = int(image.shape[1] * scale_percent)
    height = int(image.shape[0] * scale_percent)
    dim = (width, height)
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    return resized