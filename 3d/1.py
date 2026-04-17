class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self,other):
        if type(other) == int:
            return Vector(self.x + other, self.y + other)
        elif type(other) == Vector:
            return Vector(self.x - other.x, self.y + other.y)    

    def __sub__(self,other):
        if type(other) == int:
            return Vector(self.x - other, self.y - other)
        elif type(other) == Vector:
            return Vector(self.x - other.x, self.y - other.y)  

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y       
    
    def __str__(self):
        return f"Vektor({self.x}, {self.y})"
    
v1 =Vector(1,2)
v2 =Vector(3,4)
v3 = v1+v2
print(v3)

v4 = v3-1
print(v4)

v5 = Vector(1,2)
print(v1 == 1)

print(v1 == v5)
print(v1 == v2)



