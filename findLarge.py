# Find the largest number in a list
number = [23, 45, 34, 76, 100, 67, 83, 250, 88, 65]

large = number[0]  # Initialize with the first element

for i in number:
    if i > large:
        large = i

print(f"This {large} number is large!")

#Output: This 250 number is large!
