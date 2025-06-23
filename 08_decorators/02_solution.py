# Debugging Function calls
# Create a decorator to print the function name and the values of its arguments every time the function is called

def debug(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        function_name = func.__name__
        print("Function name:", function_name)
        if (args_value):
            print("Arguments:", args_value)
        if (kwargs_value):
            print("Named arguments:", kwargs_value)
        return result
    return wrapper



@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

# greet("taran", "hi")

# debug(greet)("ta ran", greeting="hi") 

greet("taran", greeting="hi")
greet("taran", "hi")