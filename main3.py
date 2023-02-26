from PIL import Image
import pytesseract
import tkinter as tk
from tkinter import filedialog

# 实例化
root = tk.Tk()

choice = int(input('请选择要是识别文字的图片：简体（1）/ 繁体（2）/ 全都要（3）：'))

# 获取文件夹路径
nowpath = filedialog.askopenfilename()
print('完成，进行下一步...')

# 识别j简体中文：chi_sim
if choice == 1:
    text = pytesseract.image_to_string(Image.open(nowpath),lang='chi_sim')
    print(text)

# 识别繁体中文：chi_tra
if choice == 2:
    text = pytesseract.image_to_string(Image.open(nowpath),lang='chi_tra')
    print(text)

# 识别出简体、繁体 都呈现
if choice == 3:
    text = pytesseract.image_to_string(Image.open(nowpath),lang='chi_sim')
    print(text)
    text = pytesseract.image_to_string(Image.open(nowpath),lang='chi_tra')
    print(text)