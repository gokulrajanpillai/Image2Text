from PIL import Image
import pytesseract

im = Image.open("images/test-image.png")

text = pytesseract.image_to_string(im, lang = 'eng')

print("Processed text result is: ",text)
