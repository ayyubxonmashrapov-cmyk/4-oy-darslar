from PyQt5.QtWidgets import *
import json

class Arenda(QWidget):
    def __init__(self, *args, **kvargs):
        super().__init__(*args,**kvargs)

        self.resize(600,400)

        grid = QGridLayout()

        self.edit_manzil = QLineEdit()
        self.edit_manzil.setPlaceholderText("Uy mazili")

        self.edit_ism = QLineEdit()
        self.edit_ism.setPlaceholderText("Ijarachi_ismi")

        self.edit_narxi = QLineEdit()
        self.edit_narxi.setPlaceholderText("ijara_narxi")

        self.edit_muddat = QLineEdit()
        self.edit_muddat.setPlaceholderText("Muddat (oy)")

        self.btn_qosh = QPushButton("Qo'shish")

        self.edit_qidiruv = QLineEdit()
        self.edit_qidiruv.setPlaceholderText("Manzil bo'ycha")
        self.btn_qidir = QPushButton("Qidirish")

        self.btn_hisob = QPushButton("Hisoblash")

        len(self.__oqi()) 
        self.lbl_result = QLabel(f"Jami ijaralar: {len(self.__oqi()) }")
        

        #events
        self.btn_qosh.clicked.connect(self.qosh)
        self.btn_qidir.clicked.connect(self.qidir)
        self.btn_hisob.clicked.connect(self.daromad_hisobla)

        #grid
        grid.addWidget(self.edit_manzil, 0,0,1,2)
        grid.addWidget(self.edit_ism, 1,0,1,2)
        grid.addWidget(self.edit_narxi, 2,0,1,2)
        grid.addWidget(self.edit_muddat, 3,0,1,2)
  
        grid.addWidget(self.btn_qosh, 4,0,1,2)

        grid.addWidget(self.edit_qidiruv, 5,0)
        grid.addWidget(self.btn_qidir, 5,1)

        grid.addWidget(self.btn_hisob, 6,0,1,2)

        grid.addWidget(self.lbl_result, 7,0,1,2)

        self.setLayout(grid)
        self.show()

    def __oqi(self):
        try:
            with open("rentals.json", "r") as file:
                return json.load(file)
        except:
            return []
        
    def __yoz(self, nimadur):
        with open("rentals.json", "w") as file:
            json.dump(nimadur, file, indent=4)
        
    def tekshir(self):
        if not self.edit_manzil.text() or not self.edit_ism.text() or not self.edit_narxi.text() or not self.edit_muddat.text():
            QMessageBox.warning(None, "xato", "Barcha maydonlarni to‘ldiring!")
            return True
        
        if len(self.edit_manzil.text()) < 5:
            QMessageBox.warning(None, "xato", "Manzil juda qisqa!")
            return True

        if not self.edit_narxi.text().isdigit():
            QMessageBox.warning(None, "xato", "Narx faqat raqam bo‘lishi kerak!")
            return True
        
        if int(self.edit_narxi.text()) <= 0:
            QMessageBox.warning(None, "xato", "Narx 0 dan katta bo‘lishi kerak!")
            return True
        
        if not self.edit_muddat.text().isdigit():
            QMessageBox.warning(None, "xato", "Muddat noto‘g‘ri! Son kiriting")
            return True
        
        if  not 1 <= int(self.edit_muddat.text()) <= 60:
            QMessageBox.warning(None,"xato", "Muddat 1–60 oy bo‘lishi kerak!") 
            return True
        
    def tozala(self):
        self.edit_manzil.setText("")
        self.edit_ism.setText("")
        self.edit_narxi.setText("")
        self.edit_muddat.setText("")    

    def qosh(self):
        manzil = self.edit_manzil.text().strip()
        ism = self.edit_ism.text().strip()
        narxi = self.edit_narxi.text().strip()
        muddat = self.edit_muddat.text().strip()

        if self.tekshir():
            return
        
        datas = self.__oqi()

        new_data = {
            "manzil" : manzil,
            "ijarachi_ismi" : ism,
            "ijara_narxi" : narxi,
            "muddat" : muddat 
        }

        datas.append(new_data)

        self.__yoz(datas)
        QMessageBox.information(None, "xabar", "kiritildi")
        self.tozala()
        self.lbl_result.setText(f"Jami ijaralar: {len(datas)}")


    def daromad_hisobla(self):
        datas = self.__oqi()
        total_income = sum([int(data["ijara_narxi"]) * int(data["muddat"]) for data in datas])
        QMessageBox.information(None, "xabar", f"{total_income} valuta")

    def qidir(self):
        manzil = self.edit_qidiruv.text().strip().lower()
        datas = self.__oqi()
        for data in datas:
            if manzil in data["manzil"].lower():
                QMessageBox.information(None, "xabar", f"{manzil.title()} | {data['ijarachi_ismi']} | {data['ijara_narxi']} | {data['muddat']}")
                return
            
        QMessageBox.information(None, "xabar", "topilmadi")
        


app = QApplication([])

a = Arenda()

app.exec()