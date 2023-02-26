################################  待测试与检测  ################################
from PIL import Image
import pytesseract
import tkinter as tk
from tkinter import filedialog

# 实例化
root = tk.Tk()

import sys
# from PyQt5.QtWidgets import QApplication ,QWidget , QGridLayout, QPushButton, QLabel
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,  QTextEdit, QGridLayout, QApplication,QPushButton)
class Winform(QWidget):
  def __init__(self,parent=None):
    super(Winform,self).__init__(parent)
    self.initUI()
  def initUI(self):
    grid = QGridLayout()
    grid.setSpacing(10)

    names = ['简体','繁体','All']

    # names1=['简体']
    # names2=['繁体']
    # names3=['All']

    #3 在网格中创建一个位置列表
    positions = [(i,j) for i in range(5) for j in range(4)]
    # 4 创建按钮并通过addWIdget（）方法添加到布局中
    for position, name in zip(positions, names):
        if name == '':
            continue
        button = QPushButton(name)
        grid.addWidget(button, *position)

    # button1 = QPushButton(names1)
    # button2 = QPushButton(names2)
    # button3 = QPushButton(names3)
    # grid.addWidget(button1, 1,0)
    # grid.addWidget(button2, 1,1)
    # grid.addWidget(button3, 1,2)

    self.move(300, 150)

    contentLabel = QLabel('识别内容')
    # titleEdit = QLineEdit()
    # authorEdit = QLineEdit()
    contentEdit = QTextEdit()

    # grid.addWidget(titleLabel, 1, 0)
    # grid.addWidget(titleEdit, 1, 1)
    # grid.addWidget(authorLabel, 2, 0)
    # grid.addWidget(authorEdit, 2, 1)
    grid.addWidget(contentLabel, 3, 0)
    grid.addWidget(contentEdit, 3, 1, 5, 1)
    self.setLayout(grid)
    self.setGeometry(300, 300, 350, 300)
    self.setWindowTitle('图像文字识别')

    # 识别j简体中文：chi_sim
    if names[1]:
        # 获取文件夹路径
        nowpath = filedialog.askopenfilename()
        text = pytesseract.image_to_string(Image.open(nowpath),lang='chi_sim')
        print(text)

    # 识别繁体中文：chi_tra
    elif names[2]:
        # 获取文件夹路径
        nowpath = filedialog.askopenfilename()
        text = pytesseract.image_to_string(Image.open(nowpath),lang='chi_tra')
        print(text)

    # 识别出简体、繁体 都呈现
    elif names[3]:
        # 获取文件夹路径
        nowpath = filedialog.askopenfilename()
        text = pytesseract.image_to_string(Image.open(nowpath),lang='chi_sim')
        print(text)
        text = pytesseract.image_to_string(Image.open(nowpath),lang='chi_tra')
        print(text)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Winform()
    form.show()
    sys.exit(app.exec_())