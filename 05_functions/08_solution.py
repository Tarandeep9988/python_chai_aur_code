# Function with **kwargs
# Create a function that accepts any number of keyword arguments and prints them in the format key : value


def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(name="Shaktiman", power="lazer", enemy="Dr. Jackaal")