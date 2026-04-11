import json



class Pult:

    def __init__(self):
        data = self.load()
        self.hozirgi_ovoz = data['hozirgi_ovoz']
        self.hozirgi_kanal = data['hozirgi_kanal']
        self.on_off = data['on_off']  
        self.mute = data['mute']  
        self.max_kanal = 100


    def yoq(self):
        if self.on_off == True:
            print("Televizor yoqiqku")
            return
        self.on_off = True
        print("Televizor yondi")   
    def ochir(self):
        if self.on_off == False:
            print("Televizor o'chiqku")
            return
        self.on_off = False
        print("Televizor o'chdi")
            

    def load(self):
        with open("pult.json") as file:
            return json.load(file)    
    def save(self, data: dict):
        with open("pult.json", "w") as file:
            json.dump(data, file)
    

    def ovozni_kotar(self):
        if not self.on_off:
            return
        if self.hozirgi_ovoz != 100:
            self.hozirgi_ovoz += 1
            self.mute = False
    def ovozni_pasaytir(self):
        if not self.on_off:
            return
        if self.hozirgi_ovoz != 0:
            self.hozirgi_ovoz -= 1
            self.mute = False
    def mute_qil(self):
        if not self.on_off:
            return
        if self.mute == False:
            self.mute = True
        else:
            self.mute = False


    def kanalga_oshir(self):
        if not self.on_off:
            return
        self.hozirgi_kanal += 1
        if self.hozirgi_kanal == 101:
            self.hozirgi_kanal = 1
    def kanalga_tushir(self):
        if not self.on_off:
            return
        self.hozirgi_kanal -= 1
        if self.hozirgi_kanal == 0:
            self.hozirgi_kanal = 100
    def kanalga_otkaz(self, soralgan_kanal):
        if not self.on_off:
            return
        if 0 < soralgan_kanal < 101:
            self.hozirgi_kanal = soralgan_kanal
        else:
            print(self.hozirgi_kanal)    


    def info(self):
        holati = "O'chiq" if self.on_off == False else "Yoqiq"
        mute = "O'chiq" if self.mute == False else "Yoqiq"
        print(f"Holati: {holati}\nKanal: {self.hozirgi_kanal}\nOvoz: {self.hozirgi_ovoz}\nMute: {mute}")

pult = Pult()
while 1:
    tanlov = int(input("""=== TV Pult ===
    1. Ovozni ko'tarish
    2. Ovozni pasaytirish
    3. Mute/Unmute                   
    4. O'chirish
    5. Yoqish
    6. Kanalga olish
    7. Kanalni oshirish
    8. Kanalni tushirish
    9. Ma'lumot
    0. Chiqish
    
          """))
    
    if tanlov == 1:
        pult.ovozni_kotar()
    elif tanlov == 2:
        pult.ovozni_pasaytir()
    elif tanlov == 3:
        pult.mute_qil()
    elif tanlov == 4:
        pult.ochir()
    elif tanlov == 5:
        pult.yoq()
    elif tanlov == 6:
        pult.kanalga_otkaz(int(input()))
    elif tanlov == 7:
        pult.kanalga_oshir()
    elif tanlov == 8:
        pult.kanalga_tushir()
    elif tanlov == 9:
        pult.info()
    elif tanlov == 0:
        pult.save({"hozirgi_ovoz": pult.hozirgi_ovoz, "hozirgi_kanal": pult.hozirgi_kanal, "on_off": pult.on_off, "mute": pult.mute})
        break