class Dog:
    def __init__(self, name, bread):
        self.name = name
        self.bread = bread

    def bark(self):
        print(f"{self.name} is berking")
        print(f"{self.bread} is berking")

dog1 = Dog("tommy", "tuffy")
dog1.bark()