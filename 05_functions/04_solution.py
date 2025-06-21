# Function returns multiple values
import math

def circle_stats(radius): 
    return math.pi * (radius ** 2), 2 * math.pi * radius


a, c = circle_stats(10)

print("Area: ", round(a, 3), "| Circumference:", round(c, 3))