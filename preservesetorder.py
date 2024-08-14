#preserve set order by saving it as another data structure

from collections import OrderedDict

my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Create an OrderedDict using the list items as keys (ensuring uniqueness) and None as values
ordered_set = OrderedDict.fromkeys(my_list)

# Convert back to a list to get unique elements in original order
unique_elements_in_order = list(ordered_set.keys())

print(unique_elements_in_order)  # Output: [3, 1, 4, 5, 9, 2, 6]

#manually order and set lookup
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

unique_elements_in_order = []
seen = set()

for item in my_list:
    if item not in seen:
        unique_elements_in_order.append(item)
        seen.add(item)

print(unique_elements_in_order)  # Output: [3, 1, 4, 5, 9, 2, 6]
