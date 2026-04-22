from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

#=======================================
app = QApplication([])
root = QWidget()

root.resize(500,500)
root.setStyleSheet("font-size: 20px")

layout = QVBoxLayout()



#=======================================
edit_line = QLineEdit()
btn = QPushButton("ok")
lbl = QLabel("matn")
lbl.setAlignment(Qt.AlignCenter)

#=======================================
layout.addWidget(edit_line)
layout.addWidget(btn)
layout.addWidget(lbl)

#=======================================
root.setLayout(layout)
root.show()
app.exec()