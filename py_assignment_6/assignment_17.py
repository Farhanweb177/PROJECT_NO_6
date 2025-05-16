def add_greeting(cls):
    def greet(self):
        return "Hello From Decorator"
    cls.greet = greet
    return cls

@add_greeting
class person:
    def __init__(self, name):
        self.name = name

p = person("Farhan")
print(p.greet())