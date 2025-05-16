class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("price cannot be nagative")
        else:
            self._price = value
    
    @price.deleter
    def price(self):
        print("price has been deleted")
        del self._price

p = Product(100)
print(p.price)

p.price = 150
print(p.price)

p.price = -50
del p.price