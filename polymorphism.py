class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} is moving.")

class Dog(Animal):
    def move(self):
        print(f"{self.name} is running.")

class Snake(Animal):
    def move(self):
        print(f"{self.name} is slithering.")

class Fish(Animal):
    def move(self):
        print(f"{self.name} is swimming.")

class Vehicle:
    def __init__(self, model):
        self.model = model

    def move(self):
        print(f"The {self.model} is moving.")

class Car(Vehicle):
    def move(self):
        print(f"The {self.model} is driving.")

class Plane(Vehicle):
    def move(self):
        print(f"The {self.model} is flying.")

# Creating instances of different classes
dog = Dog("Buddy")
snake = Snake("Slyther")
fish = Fish("Goldie")
car = Car("Sedan")
plane = Plane("Boeing 747")

# Calling the move() method on each object
animals = [dog, snake, fish]
vehicles = [car, plane]

print("Animals moving:")
for animal in animals:
    animal.move()

print("\nVehicles moving:")
for vehicle in vehicles:
    vehicle.move()
