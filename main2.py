from PIL import Image
import pytesseract
import tkinter as tk
from tkinter import filedialog

# 实例化
root = tk.Tk()

# 获取文件夹路径
print('请选择要识别文字内容的图片：')
nowpath = filedialog.askopenfilename()
print('完成，进行下一步...')

# 识别j简体中文：chi_sim
text = pytesseract.image_to_string(Image.open(nowpath),lang='chi_sim')
print(text)

# 识别繁体中文：chi_tra
text = pytesseract.image_to_string(Image.open(nowpath),lang='chi_tra')
print(text)