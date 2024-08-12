""" dir can stand for directory - analogous to a file system, or direct as in direct access. Python does not specify.
 """
 
my_list = [1, 2, 3]
print(dir(my_list))  # Output: ['append', 'clear', 'copy', ... (many more list methods)] 

import os
print(dir(os))  # Output: ['DirEntry', 'F_OK', 'MutableMapping', ... (attributes and functions in the os module)]

# Older Python 2 style (not recommended)
#f = file('my_file.txt', 'w') 
#f.write('Hello, world!')
#f.close()

"""open('my_file.txt', 'w'): opens a file named my_file.txt in write mode ('w').
If the file doesn't exist, it will be created.
If the file already exists, its contents will be overwritten (erased and replaced with new content).

as f: This assigns the opened file object to the variable f. Use f to interact with the file within the with block.

with: introduces a context manager. It ensures that the file is handled properly and automatically closed when the code block within the with statement finishes executing, even if errors occur."""

# Modern Python 3 style (recommended)
with open('my_file.txt', 'w') as f:
    f.write('Hello, world!')
    
"""
id() returns the unique identity (memory address) of an object

Object Storage: When you create a variable in Python and assign it a value (e.g., x = 10), Python doesn't directly store the value '10' in the variable itself. Instead, it creates an object in memory to hold the value '10', and the variable x essentially becomes a reference or pointer to that object's memory address.
Multiple References: Multiple variables can point to the same object in memory, sharing the same address. This is particularly relevant for immutable objects like numbers and strings, where Python optimizes memory usage by reusing existing objects when possible. For mutable objects like lists or dictionaries, changes made through one variable will be reflected in all other variables referencing the same object, as they all point to the same memory location. The built-in id() function returns the memory address (as an integer) of the object a variable refers to. You generally don't need to manipulate memory addresses directly in most Python programs -- Python's memory management system handles those details for you.

You might use the id() function for the following, but it's not as common as using other functions:

Checking if two variables refer to the same object.

Tracking object lifetime: You can use id() to observe how Python manages objects in memory, especially when dealing with mutable objects and their modifications.

Implementing Custom Data Structures or Algorithms

Hashing: In certain data structures like hash tables or dictionaries, you might use id() as a simple (though not always ideal) way to generate hash values for objects.
Object Tracking: In algorithms that involve tracking or comparing objects, id() can provide a unique identifier for each object.
Interfacing with C Extensions or Low-Level Code

Passing Object References: When interacting with C extensions or other low-level code, you might need to pass Python object references (memory addresses) to those external components. The id() function can be used to obtain these references.

The exact behavior of id() can vary across Python implementations.
"""
x = 10
y = 10

print(id(x)) 
print(id(y))  # Output: The same memory address, as small integers are often cached

list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(id(list1))
print(id(list2))  # Output: Different memory addresses, as lists are mutable objects

"""Returns the length (number of items) of a sequence (string, list, tuple, etc.)."""
   
my_string = "Hello"
my_list = [1, 2, 3, 4]

print(len(my_string))  # Output: 5
print(len(my_list))    # Output: 4


"""returns min and max"""
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

print(max(numbers))  # Output: 9
print(min(numbers))  # Output: 1

"""returns sum"""

numbers = [3, 1, 4, 1, 5, 9, 2, 6]

print(sum(numbers))  # Output: 31

