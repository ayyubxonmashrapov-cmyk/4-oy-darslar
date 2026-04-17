class BankAccount:
    def __new__(cls, *args, **kwargs):
        print("ochildi")
        return super().__new__(cls)

    def __init__(self, owner, balance):
        print("ochildi")
        self.owner = owner
        self.balance = balance

    def __del__(self):
        print("cklassdaan chiqdi")
        
    def __str__(self):
        return f"({self.owner}, {self.balance})"    
    
def printf():
    acc = BankAccount("Ali", 1000)
    print(acc)    
printf()


aca = BankAccount("Vali", 2000)
print(aca)


