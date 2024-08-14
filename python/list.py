"""
a list is a versatile and fundamental data structure used to store an ordered collection of items. These items can be of any data type, including numbers, strings, booleans, or even other lists. The defining characteristics of lists include:

Ordered: Items maintain their sequence within the list.
Mutable: You can modify the list's contents by adding, removing, or changing elements.
Heterogeneous: Lists can hold items of different data types within the same list.

"""
#create list
fruits = ["apple", "banana", "orange"]
numbers = [1, 5, 3, 9]
mixed_list = [True, "hello", 3.14, [1, 2]] 

#access elements

first_fruit = fruits[0]   # Accesses "apple"
last_number = numbers[-1] # Accesses 9

#modify list
fruits.append("grape")     # Adds "grape" to the end
numbers[1] = 7            # Changes the second element to 7
del mixed_list[0]         # Removes the first element (True)

#iterate through list

for fruit in fruits:
    print(fruit)

#count
grades = [85, 92, 78, 85, 95]
count_of_85 = grades.count(85)
print(count_of_85)  # Output: 2

#extend
list1 = [1, 2, 3]
list2 = [4, 5]
list1.extend(list2)  # Add elements of list2 to the end of list1
print(list1)         # Output: [1, 2, 3, 4, 5]

#index
colors = ["red", "green", "blue", "green"]
index_of_green = colors.index("green") 
print(index_of_green)   # Output: 1 (first occurrence)

index_of_green_after_2 = colors.index("green", 2)  
print(index_of_green_after_2)  # Output: 3

#insert
tasks = ["write report", "send email"]
tasks.insert(1, "call client")  # Insert at index 1
print(tasks)                    # Output: ["write report", "call client", "send email"] 

#pop
stack = [1, 2, 3]
last_element = stack.pop()     # Remove and return the last element
print(last_element)             # Output: 3
print(stack)                    # Output: [1, 2]

#remove
colors = ["red", "green", "blue", "green"]
colors.remove("green")  # Removes the first occurrence of "green"
print(colors)           # Output: ["red", "blue", "green"]

#clear
data = [1, 2, 3]
data.clear()  # Empty the list
print(data)   # Output: []

#reverse 
numbers = [1, 2, 3]
numbers.reverse()  # Reverse the list in-place
print(numbers)     # Output: [3, 2, 1]

#sort
words = ["banana", "apple", "cherry"]
words.sort()       # Sort alphabetically
print(words)       # Output: ["apple", "banana", "cherry"]

numbers = [3, 1, 4, 1, 5, 9]
numbers.sort(key=lambda x: abs(x - 5))  # Sort by distance from 5
print(numbers)                          # Output: [5, 4, 1, 1, 3, 9]









