import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
path = "merhaba_el_yazisi.png"
custom_config = '--oem 3 --psm 6 -l tur' #Türkçe bir metin okunacağını belirttik. 

img = cv2.imread(path)


text = pytesseract.image_to_string(img, config=custom_config) # config belirtilmezse ingilizce olarak okuma gerçekleştirir.
print(text)

"""
custom config kullanmadan daha basit bir şekilde yapmak için:

#text= pytesseract.image_to_string(img,lang="tur") kullanabilirsiniz.
"""

cv2.waitKey(0)
cv2.destroyAllWindows()

