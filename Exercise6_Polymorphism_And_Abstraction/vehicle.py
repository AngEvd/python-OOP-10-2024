from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, distance: float) -> None:
        pass

    @abstractmethod
    def refuel(self, fuel: float) -> None:
        pass


class Car(Vehicle):
    AC_CONSUMPTION = 0.9

    def __init__(self, fuel_quantity: float, fuel_consumption: float) -> None:
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: float) -> None:
        if distance * (self.fuel_consumption + Car.AC_CONSUMPTION) <= self.fuel_quantity:
            self.fuel_quantity -= distance * (self.fuel_consumption + Car.AC_CONSUMPTION)

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AC_CONSUMPTION = 1.6
    FUEL_HOLD_PERCENT = 0.95

    def __init__(self, fuel_quantity: float, fuel_consumption: float) -> None:
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: float) -> None:
        if distance * (self.fuel_consumption + Truck.AC_CONSUMPTION) <= self.fuel_quantity:
            self.fuel_quantity -= distance * (self.fuel_consumption + Truck.AC_CONSUMPTION)

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += Truck.FUEL_HOLD_PERCENT * fuel
