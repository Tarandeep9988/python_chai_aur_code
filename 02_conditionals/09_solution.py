# Leap Year Checker

year = int(input("Enter Year: "))

print(year, end=' is ')

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not Leap year")