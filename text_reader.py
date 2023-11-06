import cv2
import pytesseract
from deep_translator import GoogleTranslator, single_detection


def read_text(image_path):
    # read the image file
    img_cv = cv2.imread(image_path)

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
