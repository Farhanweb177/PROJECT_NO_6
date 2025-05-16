class Logger:
    def __init__(self):
        print("Logger Object Started")

    def __del__(self):
        print("Logger object is Distroy")

log = Logger()
