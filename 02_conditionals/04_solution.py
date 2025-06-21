# Fruit Ripeness Checker

fruit = "Banana"
color = input(f"Enter {fruit} color: ")

if fruit == "Banana":
    if color == 'Green':
        print("Unripe")
    elif color == 'Yellow':
        print("Ripe")
    elif color == 'Brown':
        print("OverRipe")
    else:
        print("Invalid Color")
else:
    print("Information not available")