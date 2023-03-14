import pytesseract as tess
import json
tess.pytesseract.tesseract_cmd = r'C:\Users\Tariq Kamal\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
from PIL import Image

img = Image.open('test_img_1.png')
text = tess.image_to_string(img)

def json_file(path, fileName, data):
    filepath = './' + path + '/' + fileName + '.json'
    with open(filepath, 'w') as fp:
        json.dump(data, fp)

path = './'
fileName = 'extracted_data'

data = {}

data['extracted_data'] = text

json_file(path, fileName, data) 