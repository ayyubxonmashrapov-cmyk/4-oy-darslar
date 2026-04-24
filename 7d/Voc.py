from operator import add
from PyQt5.QtWidgets import *

import json

def load():
    try:
        with open("sozlar.json", "r") as file:
            return json.load(file)
    except:
        with open("sozlar.son", "w") as file:
            json.dump([], file, indent=4)
            return []

def show_window(num):
    searchwindow.hide()
    showwindow.hide()
    addwindow.hide()
    mainwindow.hide()

    if num == 4:
        searchwindow.show()
    elif num == 3:
        showwindow.load_sozlar()
        showwindow.show()
    elif num == 2:
        addwindow.show()
    elif num == 1:
        mainwindow.show()

#===================================


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("QPushButton {color: red; padding: 50px; font-size: 20px;}")
        self.resize(500,500)
        layout = QVBoxLayout()

        self.btn_add = QPushButton("So'z qo'shish")
        self.btn_show = QPushButton("So'zlarni ko'rish")
        self.btn_search = QPushButton("So'zlarni qidirish")
        self.btn_exit = QPushButton("Chiqish")

        layout.addWidget(self.btn_add)
        layout.addWidget(self.btn_show)
        layout.addWidget(self.btn_search)
        layout.addWidget(self.btn_exit)

        # events
        self.btn_add.clicked.connect(lambda: show_window(2))
        self.btn_show.clicked.connect(lambda: show_window(3))
        self.btn_search.clicked.connect(lambda: show_window(4))
        self.btn_exit.clicked.connect(app.quit)

        layout.setContentsMargins(50,100,50,100)

        self.setLayout(layout)
        self.show()

class AddWindow(QWidget):
    def __init__(self):
        super().__init__()
        # self.setStyleSheet("background-color: green;")
        self.resize(500,500)
        self.setWindowTitle("So'z qo'shish")
        grid = QGridLayout()

        self.edit_uzb = QLineEdit()
        self.edit_uzb.setPlaceholderText("uzb")
        self.edit_eng = QLineEdit()
        self.edit_eng.setPlaceholderText("eng")
        self.btn_send = QPushButton("Send")

        self.btn_menu = QPushButton("menu")
        self.btn_show = QPushButton("show")
        self.btn_search = QPushButton("search")
        
        grid.addWidget(self.edit_uzb, 0,0,1,2)
        grid.addWidget(self.edit_eng, 1,0,1,2)
        grid.addWidget(self.btn_send, 0,2,2,1)
        grid.addWidget(self.btn_menu, 2,0)
        grid.addWidget(self.btn_show, 2,1)
        grid.addWidget(self.btn_search,2,2)

        # events
        self.btn_send.clicked.connect(self.add_word)
        self.btn_menu.clicked.connect(lambda: show_window(1))
        self.btn_show.clicked.connect(lambda: show_window(3))
        self.btn_search.clicked.connect(lambda: show_window(4))

        grid.setContentsMargins(50,100,50,100)

        self.setLayout(grid)
    
    def add_word(self):
        sozlar = load()

        for i in range(len(sozlar)):
            uzb = self.edit_uzb.text()
            eng = self.edit_eng.text()
            if not uzb or not eng:
                QMessageBox.warning(None,"so'z berilmadi", "lug'atni to'liq kirgizing")
                return
            if sozlar[i][0] == uzb and sozlar[i][1] == eng:            
                QMessageBox.information(None,"lug'at mavjut", "Bu lug'at avval kiritilgan")
                return
        sozlar.append([uzb,eng])

        with open("sozlar.json", "w") as file:
            json.dump(sozlar,file, indent=4)
        QMessageBox.information(None, "habar", "luga'at kiritildi")

class ShowWindow(QWidget):
    def __init__(self):
        super().__init__()
        # self.setStyleSheet("background-color: red;")
        self.resize(500,500)
        self.setWindowTitle("So'zlarni ko'rish")
        
        grid = QGridLayout()
        self.table = QTableWidget()

        self.load_sozlar()


        self.btn_menu = QPushButton("menu")
        self.btn_add = QPushButton("add new word")
        self.btn_search = QPushButton("search")

        grid.addWidget(self.table, 0,0,1,3)
        grid.addWidget(self.btn_add, 1,0)
        grid.addWidget(self.btn_menu, 1,1)
        grid.addWidget(self.btn_search,1,2)

        # events
        self.btn_add.clicked.connect(lambda: show_window(2))
        self.btn_menu.clicked.connect(lambda: show_window(1))
        self.btn_search.clicked.connect(lambda: show_window(4))

        self.setLayout(grid)

    def load_sozlar(self):
        sozlar = load()
        self.table.setRowCount(len(sozlar))
        self.table.setColumnCount(2)

        self.table.setHorizontalHeaderLabels(["uzb", "eng"])

        for i, soz in enumerate (sozlar):
            self.table.setItem(i, 0, QTableWidgetItem(soz[0]))
            self.table.setItem(i, 1, QTableWidgetItem(soz[1]))

class SearchWindow(QWidget):
    def __init__(self):
        super().__init__()
        # self.setStyleSheet("background-color: red;")
        self.resize(500,500)
        self.setWindowTitle("So'zlarni ko'rish")

        grid = QGridLayout()


        self.table = QTableWidget()

        self.load_sozlar()

        self.edit = QLineEdit()
        self.btn_menu = QPushButton("menu")
        self.btn_add = QPushButton("add new word")
        self.btn_show = QPushButton("show")

        grid.addWidget(self.edit, 0,0,1,3)
        grid.addWidget(self.table, 1,0,1,3)
        grid.addWidget(self.btn_add, 2,0)
        grid.addWidget(self.btn_show,2,1)
        grid.addWidget(self.btn_menu, 2,2)


        # events
        self.edit.textChanged.connect(self.search)
        self.btn_add.clicked.connect(lambda: show_window(2))
        self.btn_show.clicked.connect(lambda: show_window(3))
        self.btn_menu.clicked.connect(lambda: show_window(1))


        self.setLayout(grid)

    def load_sozlar(self):
        sozlar = load()
        self.table.setRowCount(len(sozlar))
        self.table.setColumnCount(2)
        
        self.table.setHorizontalHeaderLabels(["uzb", "eng"])

        for i, soz in enumerate (sozlar):
            self.table.setItem(i, 0, QTableWidgetItem(soz[0]))
            self.table.setItem(i, 1, QTableWidgetItem(soz[1]))
    
    def search(self):
        keyword = self.edit.text().strip().lower()
        self.table.clear()

        sozlar = load()
        sozlar = [soz for soz in sozlar if soz[0].startswith(keyword) or soz[1].startswith(keyword)]

        self.table.setRowCount(len(sozlar))
        self.table.setColumnCount(2)

        self.table.setHorizontalHeaderLabels(["uzb", "eng"])
        for i , soz in enumerate(sozlar):
            self.table.setItem(i, 0, QTableWidgetItem(soz[0]))
            self.table.setItem(i, 1, QTableWidgetItem(soz[1]))


app = QApplication([])
mainwindow = MainWindow()
addwindow = AddWindow()
searchwindow = SearchWindow()
showwindow = ShowWindow()

app.exec_()