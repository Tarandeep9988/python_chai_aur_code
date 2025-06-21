# Factorial Calculator

number = 200

factorial = 1

if (number < 0):
    print("Invalid number")
    exit()

while number > 0:
    factorial *= number
    number -= 1

print("Factorial:", factorial)