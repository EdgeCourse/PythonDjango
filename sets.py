# Creating sets using curly braces
fruits = {"apple", "banana", "orange"}
numbers = {1, 2, 3, 4}

# Creating a set from a list
colors_list = ["red", "green", "blue", "red"]  # Notice the duplicate 'red'
colors_set = set(colors_list)  # The set will automatically remove duplicates

print(fruits)     # Output: {'orange', 'apple', 'banana'} (order might vary)
print(numbers)    # Output: {1, 2, 3, 4}
print(colors_set) # Output: {'red', 'green', 'blue'} 

#set union
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union using the '|' operator
union_set = set1 | set2 

# Union using the 'union()' method
union_set_method = set1.union(set2)

print(union_set)        # Output: {1, 2, 3, 4, 5}
print(union_set_method) # Output: {1, 2, 3, 4, 5}

#intersection
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Intersection using the '&' operator
intersection_set = set1 & set2

# Intersection using the 'intersection()' method
intersection_set_method = set1.intersection(set2)

print(intersection_set)        # Output: {3}
print(intersection_set_method) # Output: {3}

"""
Set XOR (Symmetric Difference)

The XOR operation results in a set containing elements that are present in either of the two sets but not in both.
"""
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# XOR using the '^' operator
xor_set = set1 ^ set2

# XOR using the 'symmetric_difference()' method
xor_set_method = set1.symmetric_difference(set2)

print(xor_set)        # Output: {1, 2, 4, 5}
print(xor_set_method) # Output: {1, 2, 4, 5}


"""
Set Difference

The difference operation yields a set containing elements that are present in the first set but not in the second.
"""
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Difference using the '-' operator
difference_set = set1 - set2

# Difference using the 'difference()' method
difference_set_method = set1.difference(set2)

print(difference_set)        # Output: {1, 2}
print(difference_set_method) # Output: {1, 2}


#membership test
fruits = {"apple", "banana", "orange"}

print("apple" in fruits)   # Output: True
print("grape" in fruits)   # Output: False

#non-membership
fruits = {"apple", "banana", "orange"}

print("apple" not in fruits)   # Output: False
print("grape" not in fruits)   # Output: True


#length
fruits = {"apple", "banana", "orange"}

print(len(fruits))  # Output: 3


#add element
fruits = {"apple", "banana", "orange"}

fruits.add("grape")
print(fruits)  # Output: {'apple', 'banana', 'orange', 'grape'}

fruits.add("apple")  # No effect, as 'apple' is already present
print(fruits)  # Output: {'apple', 'banana', 'orange', 'grape'}

#clear set
fruits = {"apple", "banana", "orange"}

fruits.clear()
print(fruits)  # Output: set() (an empty set)

#shallow copy

fruits = {"apple", "banana", "orange"}

fruits_copy = fruits.copy()

print(fruits_copy)  # Output: {'apple', 'banana', 'orange'}

fruits_copy.add("grape")
print(fruits)        # Output: {'apple', 'banana', 'orange'} (original unchanged)
print(fruits_copy)   # Output: {'apple', 'banana', 'orange', 'grape'} 

#difference_update
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}

set1.difference_update(set2)
print(set1)  # Output: {1, 2} (set1 is modified in-place)


#discard
fruits = {"apple", "banana", "orange"}

fruits.discard("banana")
print(fruits)  # Output: {'apple', 'orange'}

fruits.discard("grape")  # No error, even though 'grape' is not present
print(fruits)  # Output: {'apple', 'orange'} 

#more intersection
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}

intersection_set = set1 & set2
print(intersection_set)  # Output: {3, 4}

intersection_set_method = set1.intersection(set2)
print(intersection_set_method)  # Output: {3, 4}

#disjoint
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {6, 7}

print(set1.isdisjoint(set2))  # Output: False (they share '3')
print(set1.isdisjoint(set3))  # Output: True (no common elements)

#subset
set1 = {1, 2}
set2 = {1, 2, 3, 4}

print(set1.issubset(set2))  # Output: True
print(set2.issubset(set1))  # Output: False

#superset
set1 = {1, 2, 3, 4}
set2 = {1, 2}

print(set1.issuperset(set2))  # Output: True
print(set2.issuperset(set1))  # Output: False

#pop, remove

#more symmetric difference - xor
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}

symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)  # Output: {1, 2, 5}

symmetric_difference_set_method = set1.symmetric_difference(set2)
print(symmetric_difference_set_method)  # Output: {1, 2, 5}


"""
    In Python, the difference_update() method is used to modify a set in-place by removing all elements found in another set (or any iterable). It essentially performs a set difference operation and updates the original set directly, rather than returning a new set. 
"""

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}

set1.symmetric_difference_update(set2)
print(set1)  # Output: {1, 2, 5} (set1 is modified in-place)

#the function union

#update
set1 = {1, 2, 3}
set2 = {3, 4, 5}

set1.update(set2)
print(set1)  # Output: {1, 2, 3, 4, 5} (set1 is modified in-place)

#get
person = {"name": "Alice", "age": 30, "city": "New York"}

print(person.get("age"))        # Output: 30
print(person.get("country"))     # Output: None
print(person.get("country", "USA"))  # Output: USA -sets

person = {"name": "Alice", "age": 30, "city": "New York"}

#items
for key, value in person.items():
    print(f"{key}: {value}")

person = {"name": "Alice", "age": 30, "city": "New York"}
new_info = {"age": 31, "country": "USA"}

person.update(new_info)
print(person)  
# Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'country': 'USA'} 

#set default
person = {"name": "Alice", "age": 30}

person.setdefault("city", "London")
print(person)  
# Output: {'name': 'Alice', 'age': 30, 'city': 'London'}

person.setdefault("age", 40)  # No change, 'age' already exists
print(person)  
# Output: {'name': 'Alice', 'age': 30, 'city': 'London'}

#keys
person = {"name": "Alice", "age": 30, "city": "New York"}

keys = person.keys()
print(keys)  # Output: dict_keys(['name', 'age', 'city'])

#copy
person = {"name": "Alice", "age": 30, "city": "New York"}

person_copy = person.copy()
person_copy["age"] = 31

print(person)      # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(person_copy) # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}


#key existene
person = {"name": "Alice", "age": 30, "city": "New York"}

# Deprecated: 
# if person.has_key("age"): 

# Recommended:
if "age" in person:
    print("Age is present")


#fromkeys
keys = ["name", "age", "city"]
default_value = "Unknown"

person = dict.fromkeys(keys, default_value)
print(person)  
# Output: {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}

#popitem removes a random key value pair!