from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import Qt

def bosildi5():
    matn.setText(f"{matn.text()}5")

def bosildi6():
    matn.setText(f"{matn.text()}6")

def uchir():
    matn.setText(f"{matn.text()[0:-1]}")

app = QApplication(sys.argv)
w = QWidget()
w.resize(500,500)

yozuv = QLabel("sadfasf", w)
yozuv.move(120,120)


button = QPushButton("5", w)
button.move(50,50)
button.clicked.connect(bosildi5)

button = QPushButton("6", w)
button.move(0,50)
button.clicked.connect(bosildi6)

button = QPushButton("del", w)
button.move(0,50)
button.clicked.connect(uchir)

matn = QLineEdit("", w)
matn.setPlaceholderText("Ismingizni yozing")


button.move(100,100)

# edit = QTextEdit("", w)
# edit.setPlaceholderText("Ismingizni yozing")
# button.move(200,200)

ch = QCheckBox("O'qiysizmi?", w)
ch.move(250,250)

ch1 = QRadioButton("50", w)
ch1.move(250,270)
ch2 = QRadioButton("100", w)
ch2.move(250,290)

cmb = QComboBox(w)
cmb.addItems(["1-kurs","2-kurs","3-kurs"])
cmb.move(250, 310)




w.show()

sys.exit(app.exec_())