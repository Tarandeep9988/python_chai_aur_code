# Sum of even Numbers

n = 10

sum_even = 0

for num in range(2, n + 1): 
    if num % 2 == 0:
        sum_even += num

print("The sum of even till", n, "is", sum_even)