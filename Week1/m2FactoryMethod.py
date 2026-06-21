from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car engine started")


class Truck(Vehicle):
    def start(self):
        print("Truck engine started")

class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self):
        pass

class CarFactory(VehicleFactory):
    def create_vehicle(self):
        return Car()

class TruckFactory(VehicleFactory):
    def create_vehicle(self):
        return Truck()

CarFacto = CarFactory()
car = CarFacto.create_vehicle()
car.start()

TruckFacto = TruckFactory()
truck = TruckFacto.create_vehicle()
truck.start()