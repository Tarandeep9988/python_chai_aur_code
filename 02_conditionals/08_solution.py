# Password Strength Checker

password = input("Enter password: ").strip()

len = len(password)

if len < 6:
    strength = 'Weak'
elif len <= 10:
    strength = 'Medium'
else:
    strength = 'Strong'

print("Password strength:", strength)