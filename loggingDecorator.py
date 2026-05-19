from functools import wraps

def log_Activity():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Function '{func.__name__}' is about to be called.")
            result = func(*args, **kwargs)
            print(f"Function '{func.__name__}' has been called.")
            return result
        return wrapper
    return decorator

def brew_chai():
    print("Brewing a cup of chai...")
@log_Activity()
def brew_coffee():
    print("Brewing a cup of coffee...")