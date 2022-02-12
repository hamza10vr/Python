

from turtle import speed


class Vehicle():
    def __init__(self,bodystyle):
        self.bodystyle = bodystyle

    def Driving(self,speed):
        self.mode = "Automatic"
        self.speed = speed

class Car(Vehicle):
    def __init__(self,enginetype):
        super().__init__("CAR")
        self.wheel =4
        self.door = 4
        self.engine = enginetype

    def Driving(self, speed):
        super().Driving(speed)
        print("My ", self.mode, " ", self.engine , " ", self.bodystyle, "is traveling at ", self.speed)

car1 = Car("gas")
car1.Driving(20)