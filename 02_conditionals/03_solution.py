# Grade Calculator

score = int(input("Enter score: "))

if score > 100 or score < 0:
    print("Invalid Grade")
    exit()


if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(grade, 'Grade')