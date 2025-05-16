class Car:
    def __init__ (self, brand):
        self.brand = brand

    def show_car(self):
        print(f"{self.brand} car is starting")

c1 = Car("civic")
print(c1.brand)
c1.show_car()