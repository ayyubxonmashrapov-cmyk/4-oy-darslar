class Book:
    def __init__(self, name: str, author: str, year: int):
        self.name = name
        self.author = author
        self.year = year

    def info(self):
        print(f"kitob nomi - {self.name}\nmuallif - {self.author}\n{self.year}")

b1 = Book("alkimiyo", "Paulo Koelyo", 9999)
# print(b1.name,"-", b1.author)        
b1.info()

