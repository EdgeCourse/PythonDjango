"""
Slicing creates a new list, leaving the original list unchanged.
new_list = original_list[start:stop:step]

start: The index where the slice begins (inclusive). Defaults to 0 if omitted.
stop: The index where the slice ends (exclusive). Defaults to the length of the list if omitted.
step: The number of indices to jump between elements. Defaults to 1 if omitted.

Tuples are often preferred when you want to ensure that the data remains constant and protected from accidental modification. They are commonly used for:

Representing coordinates, dates, or other fixed combinations of values.
Function arguments or return values where you want to group multiple pieces of data.
Keys in dictionaries, as they need to be hashable (immutable).
"""
#slice a list
numbers = [10, 20, 30, 40, 50]

# Get the first three elements
first_three = numbers[:3]  # Equivalent to numbers[0:3]
print(first_three)  # Output: [10, 20, 30]

# Get the last two elements
last_two = numbers[-2:] 
print(last_two)  # Output: [40, 50]

# Get every other element
every_other = numbers[::2]
print(every_other)  # Output: [10, 30, 50]

# Reverse the list
reversed_list = numbers[::-1]
print(reversed_list)  # Output: [50, 40, 30, 20, 10]

#slice a tuple 
coordinates = (10, 20, 30, 40, 50)

# Get the first three elements
first_three = coordinates[:3] 
print(first_three)  # Output: (10, 20, 30)

# Get the last two elements
last_two = coordinates[-2:] 
print(last_two)  # Output: (40, 50)

# Get every other element
every_other = coordinates[::2]
print(every_other)  # Output: (10, 30, 50)

# Reverse the tuple
reversed_tuple = coordinates[::-1]
print(reversed_tuple)  # Output: (50, 40, 30, 20, 10)

