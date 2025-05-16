class TemperatureConverter:
    @staticmethod
    def celsius_fahrenheit(c):
        return (c * 9/5) + 32
    
result = TemperatureConverter.celsius_fahrenheit(20)
print(f"20c is equal to {result}F")