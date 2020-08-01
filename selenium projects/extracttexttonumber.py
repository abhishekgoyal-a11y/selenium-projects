import pytesseract
from PIL import Image


def textotnumber(path):
    pytesseract.pytesseract.tesseract_cmd = r'D:/Program Files/Tesseract-OCR/tesseract.exe'
    img = Image.open(path)
    text = pytesseract.image_to_string(img)
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    a = 0
    lists = []
    while a < len(text):
        for i in range(10):
            if text[a] == number[i]:
                lists.append(text[a])
        a += 1
    x = ""
    for j in lists:
        x += j
    return x
