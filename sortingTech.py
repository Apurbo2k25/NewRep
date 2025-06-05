# Sorting the list in Ascending Order

numbers = [23, 45, 34, 76, 100, 67, 83, 250, 88, 65]
numbers.sort()
print(f"Here is Your Sorted list: {numbers}")
#Here is Your Sorted list: [23, 34, 45, 65, 67, 76, 83, 88, 100, 250]


# Reversing the list

numbers.reverse()
print(f"Here is Your Reversed list: {numbers}")
#Here is Your Reversed list: [250, 100, 88, 83, 76, 67, 65, 45, 34, 23]


# Reverse Without reverse() method

reversed_numbers = []
for i in range(len(numbers) - 1, -1, -1):
    reversed_numbers.append(numbers[i])
print("Reversed list:", reversed_numbers)
#Reversed list: [23, 34, 45, 65, 67, 76, 83, 88, 100, 250]


# List Comprehensions
# Create a list of cubes from 1 to 5
squares = [x**3 for x in range(1, 6)]
print(squares) 
# Output: [1, 8, 27, 64, 125]

