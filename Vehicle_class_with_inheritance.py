

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
        self.wheels =4
        self.doors = 4
        self.engine = enginetype

    def Driving(self, speed):
        super().Driving(speed)
        print("My ", self.mode, " ", self.engine , " ", self.bodystyle, "is traveling at ", self.speed," it has ", self.wheels, " and ", self.doors, " doors!")


class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcycle")
        if hassidecar:
            self.wheels =3
        else:
            self.wheels = 2

        self.doors = 0 
        self.engine = enginetype
    
    def Driving(self, speed):
        super().Driving(speed)
        print("My ", self.mode, " ", self.engine , " ", self.bodystyle, "is traveling at ", self.speed," it has ", self.wheels, " and ", self.doors, " doors!")



car1 = Car("gas")
car1.Driving(20)

mtc = Motorcycle("electric", True)
mtc.Driving(45)

mtc = Motorcycle("electric", False)
mtc.Driving(45)