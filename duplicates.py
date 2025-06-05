# Removing Duplicates from a List

# Original list with duplicate values
numbers = [1, 2, 2, 3, 4, 4, 5]

# Convert the list to a set to remove duplicates (sets don't allow duplicates)
# Then, convert it back to a list
unique_numbers = list(set(numbers))

# Print the final list without duplicates
print("List without duplicates:", unique_numbers)


#Output: List without duplicates: [1, 2, 3, 4, 5]
