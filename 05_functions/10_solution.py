# Recursive Function
# Calculate factorial of a number

def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number - 1)


print(factorial(1000))