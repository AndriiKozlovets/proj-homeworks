class Car:
    def __init__(self, brand, model, year, speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = max(speed, 0)

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed = max(self.speed - 5, 0)

    def display_info(self):
        return f"Car Info: {self.brand} {self.model} {self.year}"

    def display_speed(self):
        return f"Speed: {self.speed} km/h"


# Example usage:
my_car = Car('Lamborghini', 'Urus', 2020, 0)

print(my_car.display_info())  # Output: Car Info: Toyota Camry 2020

# Accelerate
my_car.accelerate()
print(my_car.display_speed())  # Output: Speed: 5 km/h

# Accelerate
my_car.accelerate()
print(my_car.display_speed())  # Output: Speed: 10 km/h

# Brake
my_car.brake()
print(my_car.display_speed())  # Output: Speed: 5 km/h

# Brake
my_car.brake()
print(my_car.display_speed())  # Output: Speed: 0 km/h
