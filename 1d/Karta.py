class Karta:
    def __init__(self, egasi, raqami, sanasi="10.04.2026", kompaniya="Agro Bank", balans=0):
        self.balans = balans
        self.kompaniya = kompaniya
        self.egasi = egasi
        self.sanasi = sanasi
        self.raqami = raqami
    
    def pul_tushir(self, summa):
        if summa > 1_000_000:
            print("Mumkin emas")
        else:
            self.balans += summa
    
    def pul_naqt_qil(self, summa):
        if self.balans < summa:
            return "Xato: mabalnsda etarli mablag yoq"
        if summa < 10000: 
            return "Xato: kamida 10000"
        if summa%5000 != 0:
            return "Xato: noto'gri summa"
        self.balans -= summa
    
    # def balans(self):
    #     return self.balans



kumush_karta = Karta("Kumush", 1234_4567_7896_4342, balans=2000)
kumush_karta.pul_tushir(100000)
print(kumush_karta.balans)