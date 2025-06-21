# Given a string, find the first non-repeated character

str = "teeter"

ans = "There is no non repeating character"
for char in str:
    if str.count(char) == 1:
        ans = char + " is the first non repeating character"
        break
print(ans)