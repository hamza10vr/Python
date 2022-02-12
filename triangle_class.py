

class Triangle():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def CalculateParameter(self):
        return self.a + self.b + self.c

tri1 = Triangle(1,2,3)
tri2 = Triangle(2,3,4)

print(tri1.CalculateParameter())
print(tri2.CalculateParameter())