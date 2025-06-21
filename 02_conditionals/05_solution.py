# Weather Activity Suggestion
weather = input("Enter weather: ").lower()

if weather == 'sunny':
    activity = "Go for a walk"
elif weather == 'rainy':
    activity = 'Read a Book'
elif weather == 'snowy':
    activity = 'Build a snowman'
else:
    print("Invalid weather")
    exit()

print(activity)