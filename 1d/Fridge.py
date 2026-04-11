class Fridge:
    def __init__(self, model: str, harorat=2, ichidagi_mahsulotlar=[]):
        self.model = model
        self.harorat = harorat
        self.ichidagi_mahsulotlar = ichidagi_mahsulotlar

    def info(self):
        print(f"{self.harorat}, {self.ichidagi_mahsulotlar}")

    def mahsulot_qosh(self, name: str | list[str]):
        if type(name) == str:
            self.ichidagi_mahsulotlar.append(name)
        else:
            self.ichidagi_mahsulotlar.extend(name)

    def mahsulot_chiqaz(self, name: str) -> None | False:
        if name in self.ichidagi_mahsulotlar:
            self.ichidagi_mahsulotlar.remove(name)
        else:
            return False    
        
    def set_harorat(self, yangi_harorat):
        self.harorat = yangi_harorat
    
fridge1 = Fridge("Samsung")

fridge1.info()  

fridge1.mahsulot_qosh("apple")
fridge1.info()  

fridge1.mahsulot_qosh(["banana", "milk", "egg"])
fridge1.info()  

fridge1.mahsulot_chiqaz("milk")
fridge1.info()  

result = fridge1.mahsulot_chiqaz("cola")
print(result)  

fridge1.set_harorat(5)
fridge1.info()  
