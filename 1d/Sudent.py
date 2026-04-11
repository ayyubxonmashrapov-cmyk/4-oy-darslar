class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def salomlash(self):
        print(f"Assalamu alaykum mening ismim {self.name}, yoshim {self.age}da")    

s1 = Student("Ali", 20)
print(s1.name, s1.age)
s1.salomlash()
