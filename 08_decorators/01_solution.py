# Timing function Execution
# Write a decorator that measures the time a function takes to execute

import time


# This syntax is as it is followed
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end - start} time")
        return result
    return wrapper


# def example_function(n):
#     time.sleep(n)


# example_function(2)
# timer(example_function)(5)


# Made a dicorator
@timer
def example_function(n):
    time.sleep(n)

example_function(2)