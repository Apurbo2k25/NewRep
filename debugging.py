def find_largest(numbers):

    largest = 0  # Error: Should initialize to the first element in the list

    for num in numbers:

        if num > largest:

            largest == num  # Error: Should use =, not ==

    return largest


numbers = [3, 5, 2, 8, 1]

print("The largest number is", findLargest(numbers))