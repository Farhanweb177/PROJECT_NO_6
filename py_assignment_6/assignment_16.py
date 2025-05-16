def log_function_call(func):
    def wrapper():
        print("function is being called")
        func()
    return wrapper
    
@log_function_call
def say_hello():
    print("Hello, Farhan!")

say_hello()