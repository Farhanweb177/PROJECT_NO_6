class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor
    
multiplier = Multiplier(6)

print(callable(multiplier))
result = multiplier(16)
print(result)