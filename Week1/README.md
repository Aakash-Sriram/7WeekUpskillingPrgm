## Task 1 

# Exercise name: Implement Singleton Pattern in Python

Demonstrate the Singleton Design Pattern by ensuring that **only one** instance of a class can be created.

```
def __new__(cls):
    if cls._instance is None:  
        cls._instance = super().__new__(cls)
    return cls._instance
```

-> _instance is a class variable that stores the single object.

-> Initially _instance is None because no object exists yet.

-> cls refers to the class itself.

-> __new__() is overridden to control object creation.

-> If no instance exists, a new object is created and stored.

-> Otherwise, the existing object is returned.

# output
![alt text](image.png)



## Task 2

# Exercise name: Apply Factory Method Pattern — Vehicle Factory
Demonstrate the Factory Method Design Pattern using different vehicle types.

```
TruckFacto = TruckFactory()
truck = TruckFacto.create_vehicle()
truck.start()
```


-> VehicleFactory declares the factory method.

-> CarFactory creates Car objects.

-> BikeFactory creates Bike objects.

-> The client uses factories instead of creating vehicles directly.

-> New vehicle types can be added without changing existing code.

# output

![alt text](image-1.png)


## Task 3