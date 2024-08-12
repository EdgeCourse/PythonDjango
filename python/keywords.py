# is, not
x = 5
y = 5
z = 10

print(x is y)  # True (same object)
print(x is not z)  # True (different objects)

# lambda
square = lambda x: x * x
print(square(4))  # 16

# nonlocal
def outer_function():
    x = 10
    def inner_function():
        nonlocal x
        x += 5
    inner_function()
    print(x)  # 15

outer_function()

# try, except, finally, raise
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Error: Division by zero!")
finally:
    print("This will always execute, even after an exception.")

def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")

# while
count = 0
while count < 5:
    print(count)
    count += 1

# with (context manager for file handling)
with open("data.txt", "r") as file:
    contents = file.read()
    print(contents)

# or
name = ""
if name == "" or name is None:
    print("Name is missing!")

# yield (generator function)
def even_numbers(limit):
    for i in range(limit):
        if i % 2 == 0:
            yield i

for num in even_numbers(10):
    print(num)


# False, True, None
is_valid = True
if not is_valid:
    print("Invalid data!")
else:
    result = None  # Initialize result to None
    # ... perform some operation that might assign a value to result

# class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person = Person("Alice", 30)
person.greet()

# continue
for i in range(10):
    if i % 2 == 0:  # Skip even numbers
        continue
    print(i)  # Print odd numbers

# for
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num * 2)

# from, import
from math import sqrt, pi

print(sqrt(16))
print(pi)


# and, as
x = 10
y = 5
if x > 0 and y > 0:
    print("Both x and y are positive.")

import numpy as np  # Import numpy and give it the alias 'np'
arr = np.array([1, 2, 3])
print(arr)

# assert
def divide(a, b):
    assert b != 0, "Cannot divide by zero!"
    return a / b

result = divide(10, 2)
print(result)

# break
while True:
    user_input = input("Enter a number (or 'q' to quit): ")
    if user_input == 'q':
        break
    print("You entered:", user_input)

# del
my_list = [1, 2, 3, 4]
del my_list[2]  # Delete the element at index 2
print(my_list)

# elif, else
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C or below")


# global
global_var = 10

def modify_global():
    global global_var
    global_var += 5

modify_global()
print(global_var)

# if
age = 18
if age >= 18:
    print("You are an adult.")

# in
fruits = ["apple", "banana", "orange"]
if "banana" in fruits:
    print("Banana is in the list.")

# import, pass
import random

# This function doesn't do anything yet, but we use 'pass' as a placeholder
def do_something():
    pass

print(random.randint(1, 10))


# Built-in functions and classes used as identifiers
# (Generally not recommended, but demonstrating the concept)

len = 5  # Overwrites the built-in len() function
print(len)  # Output: 5 (no longer the len() function)

int = "hello"  # Overwrites the built-in int() class
print(int)  # Output: hello (no longer the int() class)
