class Contact:
    def __init__(self, number: int, name: str, email: str):
        self.number = number
        self.name = name
        self.email = email

    def info(self) -> str:
        print(f"{self.name}\n{self.number}\n{self.email}")

    def chenge_mail(self, new_mail: str) -> None:
        self.email = new_mail

c1 = Contact(998901876965, "Ayyub", "ayyubxonmashrapov@gmail.com")        
c1.info()
c1.chenge_mail("mashrapovayyubxon@gmail.com")
c1.info()