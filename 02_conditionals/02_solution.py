# Movie Ticket Pricing

age = int(input("Enter age: "))
day = input("Enter day: ")

price = 12 if age >= 18 else 8

price -= 2 if day.lower().strip() == 'wednesday' else 0

print("Ticket price for you is $", price)