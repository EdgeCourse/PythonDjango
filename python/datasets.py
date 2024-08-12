"""
Lists: When you need an ordered collection that can change over time.
Tuples: When you need an ordered, immutable collection.
Sets: When you need an unordered collection with no duplicates.
Frozen Sets: When you need an immutable set (e.g., to use as a dictionary key).
Dictionaries: When you need to store key-value pairs and access values by their associated keys.

Sequences vs. Data Structures:

All of these are considered data structures, which are ways of organizing and storing data in a computer's memory.
Lists and tuples are also specifically categorized as sequences because they maintain a specific order of elements and allow accessing elements by their position (index).

   
Sets and frozen sets are not sequences, as they are unordered collections.   
Dictionaries are also not sequences, as they store data as key-value pairs and access is done through keys, not positions.   
Commonalities:

Iterable: All of them are iterable, meaning you can loop through their elements using a for loop.
Container Types: They are all container types, meaning they can hold multiple values or elements.   
Built-in Constructors: Each has a corresponding built-in constructor function (e.g., list(), tuple()) to create instances of that type.
Accept Iterables: Most of their constructors can take an iterable (like a list or a string) as an argument to create a new instance populated with elements from that iterable.



1. Lists

Mutable: You can change their contents after creation (add, remove, modify elements).
Ordered: Elements maintain their insertion order.
Allows Duplicates: Can contain multiple instances of the same value.
Syntax: Enclosed in square brackets []
"""


my_list = [1, 2, 3, "apple", 2]  # Mixed data types, duplicates allowed
my_list.append(4)  # Add an element
my_list[0] = 10   # Modify an element
print(my_list)   # Output: [10, 2, 3, 'apple', 2, 4]

"""
2. Tuples

Immutable: You cannot change their contents after creation.
Ordered: Elements maintain their insertion order.
Allows Duplicates: Can contain multiple instances of the same value.
Syntax: Enclosed in parentheses () (often optional)
"""

my_tuple = (1, 2, 3, "apple", 2)
# my_tuple[0] = 10  # This would raise an error, as tuples are immutable
print(my_tuple)    # Output: (1, 2, 3, 'apple', 2)

"""
3. Sets

Mutable: You can add or remove elements after creation.
Unordered: Elements have no specific order.
No Duplicates: Automatically removes duplicate values.
Syntax: Enclosed in curly braces {} or created using the set() constructor.
"""

my_set = {1, 2, 3, "apple", 2}
my_set.add(4)
print(my_set)   # Output: {1, 2, 3, 4, 'apple'} (duplicates removed, order might vary)

"""
4. Frozen Sets

Immutable: Like tuples, but unordered and with no duplicates.
Syntax: Created using the frozenset() constructor.
"""

my_frozenset = frozenset([3, 1, 4, 1])
# my_frozenset.add(2)  # This would raise an error, as frozen sets are immutable
print(my_frozenset)  # Output: frozenset({1, 3, 4})

"""
5. Dictionaries

Mutable: You can add, remove, or modify key-value pairs after creation.
Unordered (before Python 3.7): Key-value pairs had no specific order.
Ordered (Python 3.7 and later): Key-value pairs maintain their insertion order.
No Duplicate Keys: Each key must be unique.
Syntax: Enclosed in curly braces {} with key-value pairs separated by colons, or created using the dict() constructor.
"""

my_dict = {"name": "Alice", "age": 30}
my_dict["city"] = "New York"  # Add a new key-value pair
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

