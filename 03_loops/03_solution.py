# Mutiplication table skipping 5

number = 3

for i in range(1, 11):
    if i == 5:
        # Skip it
        print("Skipping 5")
        continue
    print(number, "X", i, "=", number * i)