# Count the number of even numbers in a list
count = 0
number = [23, 45, 34, 76, 100, 67, 83, 250, 88, 65]

for i in number:
    if i % 2 == 0:
        count += 1

print("Even numbers count:", count)

#Output: Even numbers count: 5
