from abc import ABC

from homework_02.exceptions import LowFuelError, NotEnoughtFuel


class Vehicle(ABC):
    
    def __init__(self, weight=1500, started=False, fuel=0, fuel_consumtion=10 ):
        # fuel_consumtion в расчете на 1 у.е. distatnce
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumtion = fuel_consumtion
    
    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance):
        if self.fuel > self.fuel_consumtion * distance:
            self.fuel -= self.fuel_consumtion * distance
        else:
            raise NotEnoughtFuel
