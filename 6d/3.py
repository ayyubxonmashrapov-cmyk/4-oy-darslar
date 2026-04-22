from PyQt5.QtWidgets import *

app = QApplication([])
root = QWidget()

grid = QGridLayout()
#=====================================
input_edit = QLineEdit()

btn1 = QPushButton("1")
btn2 = QPushButton("2")
btn3 = QPushButton("3")
btn_plus = QPushButton("+")

btn4 = QPushButton("4")
btn5 = QPushButton("5")
btn6 = QPushButton("6")
btn_minus = QPushButton("-")

btn7 = QPushButton("7")
btn8 = QPushButton("8")
btn9 = QPushButton("9")
btn_mul = QPushButton("*")

btn0 = QPushButton("0")
btn_bol = QPushButton("/")

#=====================================
grid.addWidget(input_edit, 0,0, 1,3)

grid.addWidget(btn1, 1,0)
grid.addWidget(btn2, 1,1)
grid.addWidget(btn3, 1,2)
grid.addWidget(btn_plus, 1,3)

grid.addWidget(btn4, 2,0)
grid.addWidget(btn5, 2,1)
grid.addWidget(btn6, 2,2)
grid.addWidget(btn_minus, 1,3)

grid.addWidget(btn7, 3,0)
grid.addWidget(btn8, 3,1)
grid.addWidget(btn9, 3,2)
grid.addWidget(btn_mul, 3,3)


grid.addWidget(btn0, 4,1)
grid.addWidget(btn_bol, 4,3)


#=====================================
root.setLayout(grid)
root.show()
app.exec()


# 4,5