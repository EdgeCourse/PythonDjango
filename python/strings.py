# in to search one string for another
text = "Python is a powerful language."
is_python_present = "Python" in text
print(is_python_present)  # Output: True


# Concatenation using + operator
message = "Hello" + " " + "world!"
print(message)  # Output: Hello world!

# Indexing and Slicing
name = "Alice"
first_letter = name[0]  # Access the first character (index 0)
last_letter = name[-1]  # Access the last character (index -1)
substring = name[1:4]  # Get a substring from index 1 to 3 (excluding index 4)

print(first_letter)  # Output: A
print(last_letter)  # Output: e
print(substring)  # Output: lic

# Repetition using * operator
repeated_string = "Ha" * 3  # Repeat the string 3 times
print(repeated_string)  # Output: HaHaHa

# Membership using `in` operator
text = "Python is a powerful language."
is_python_present = "Python" in text
print(is_python_present)  # Output: True

# String formatting (f-strings)
greeting = f"Hello, {name}!"
print(greeting)  # Output: Hello, Alice!

# Methods
# Lowercase conversion using `lower()`
lowercased_message = message.lower()
print(lowercased_message)  # Output: hello world!

# Uppercase conversion using `upper()`
uppercased_message = message.upper()
print(uppercased_message)  # Output: HELLO WORLD!

# Splitting a string into a list using `split()`
words = message.split()  # Split on whitespace by default
print(words)  # Output: ['Hello', 'world!']

# Finding a substring using `find()`
position = message.find("world")  # Find the index of the first occurrence
print(position)  # Output: 6

# Replacing parts of a string using `replace()`
new_message = message.replace("world", "Python")
print(new_message)  # Output: Hello Python!

# Checking if a string starts or ends with a substring using `startswith()` and `endswith()`
starts_with_hello = message.startswith("Hello")
ends_with_exclamation = message.endswith("!")

print(starts_with_hello)  # Output: True
print(ends_with_exclamation)  # Output: True

# Stripping whitespace from the beginning and end using `strip()`
message_with_spaces = "  Hello world!  "
stripped_message = message_with_spaces.strip()
print(stripped_message)  # Output: Hello world!
