class Student:
    def __init__(self, name: str, kurs: int, ball: int):
        self.name = name
        self.kurs = kurs
        self.ball = ball

    def stependiya(self) -> bool:
        if self.ball >=4:
            return 1
        else:
            return 0  

t1 = Student("Otabek", 3, 2)
print(t1.stependiya())    