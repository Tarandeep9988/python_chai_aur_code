# Function with *args
# Write a function that takes variable number of arguments and returns their sum

def sum_all(*args):
    print(type(args))
    return sum(args)

print(sum_all(1, 2))
# print(sum_all(1, 2, 3))
# print(sum_all(1, 2, 4, 5, 3, 5, 2, 3))