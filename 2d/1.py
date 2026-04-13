class Person:
    def __init__(self, name, adres):
        self.name = name
        self.adres = adres

    def get_name(self):
        return self.name
    
    def get_adres(self):
        return self.adres
    
    def set_adres(self, new_adres):
        self.adres = new_adres

    def __str__(self):
        return f"{self.name}({self.adres})"


class Student(Person):
    def __init__(self, name, adres):
        super().__init__(name, adres)
        self.fanlar = []
        self.grades = []

    def add_course_grade(self, fan, grade):
        self.fanlar.append(fan)
        self.grades.append(grade)

    def print_grades(self):
        for fan, baho in zip(self.fanlar, self.grades):
            print(f"{fan:<10} {baho}")

    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"Student: {self.name}({self.adres})"


class Teacher(Person):
    def __init__(self, name, adres):
        super().__init__(name, adres)
        self.courses = []

    def add_course(self, course):
        if course in self.courses:
            return False
        self.courses.append(course)
        return True

    def remove_course(self, course):
        if course not in self.courses:
            return False
        self.courses.remove(course)
        return True

    def __str__(self):
        return f"Teacher: {self.name}({self.adres})"




s1 = Student("Ali", "Tashkent")
s1.add_course_grade("Math", 90)
s1.add_course_grade("English", 80)

s2 = Student("Vali", "Samarkand")
s2.add_course_grade("Physics", 85)
s2.add_course_grade("Chemistry", 75)

print(s1)
s1.print_grades()
print("O'rtacha baho:", s1.get_average_grade())

print()

print(s2)
s2.print_grades()
print("O'rtacha baho:", s2.get_average_grade())

print("\n" + "="*30)

t1 = Teacher("Gulbahor", "Samarqand")
t1.add_course("Math")
t1.add_course("Physics")
t1.remove_course("Math")

t2 = Teacher("Dilshod", "Tashkent")
t2.add_course("English")

print(t1)
print(t2)
