def my_decorator(func):
    def wrapper():
        print("Before Function runs")
        func(greet())
        print("After function runs")
    return wrapper

@my_decorator
def greet():
    print("Hi I am Goku")