from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)
w = QWidget()
w.resize(500,500)

w.show()

sys.exit(app.exec_())