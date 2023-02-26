from PIL import Image
import pytesseract

# 识别j简体中文：chi_sim
text = pytesseract.image_to_string(Image.open('简体.jpg'),lang='chi_sim')
print(text)

# 识别繁体中文：chi_tra
text = pytesseract.image_to_string(Image.open('繁体.jpg'),lang='chi_tra')
print(text)