from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

#=======================================
app = QApplication([])
root = QWidget()

root.resize(500,500)
root.setStyleSheet("font-size: 30px")

layout = QVBoxLayout()

#=======================================
lbl1 = QLabel("Login")                               #1

login_edit = QLineEdit()                             #2
login_edit.setPlaceholderText("Loginni kiriting")

lbl2 = QLabel("Parol")                               #3

parol_edit = QLineEdit()                             #4
parol_edit.setPlaceholderText("Parolni kiriting")

btn = QPushButton("Kirish")                          #5
#=======================================
layout.addWidget(lbl1)                               #1
layout.addWidget(login_edit)                         #2
layout.addWidget(lbl2)                               #3
layout.addWidget(parol_edit)                         #4
layout.addWidget(btn)                                #5

#=======================================
root.setLayout(layout)
root.show()
app.exec()