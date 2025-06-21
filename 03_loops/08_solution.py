# Prime Number Checker

number = 3

is_prime = True

if number > 1:
    for i in range(2, number):
        if (i * i > number):
            break
        if (number % i) == 0:
            is_prime = False
            break
else:
    is_prime = False

print("Number is prime" if is_prime else "Number is not prime")