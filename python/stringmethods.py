# Create a sample string
text = "  ThIs Is a MiXeD-cAsE sTrinG wItH soMe    wHitEspacE.  "

# capitalize(): Capitalizes the first letter, makes the rest lowercase
capitalized_text = text.capitalize()
print("capitalize():", capitalized_text) 

# casefold(): Converts to lowercase, even handling some special cases for caseless comparisons
casefolded_text = text.casefold()
print("casefold():", casefolded_text) 

#casefold() vs. lower(): casefold is mre aggressive and handles non-ASCII 
text = "Straße"  # German word with 'ß' (eszett)

print(text.lower())     # Output: straße
print(text.casefold())  # Output: strasse 


# center(): Centers the string within a given width, using a fill character (default is space)
centered_text = text.center(50, '*')
print("center():", centered_text)

# count(): Counts occurrences of a substring
substring_count = text.count("s")
print("count('s'):", substring_count)  

# encode(): Encodes the string using a specified encoding (default is UTF-8)
encoded_text = text.encode('utf-16')
print("encode('utf-16'):", encoded_text) 

# endswith(): Checks if the string ends with a specified suffix
ends_with_space = text.endswith(" ")
print("endswith(' '):", ends_with_space) 

# expandtabs(): Replaces tab characters with spaces (default tab size is 8)
text_with_tabs = "Hello\tworld!\tHow are you?"
expanded_text = text_with_tabs.expandtabs()
print("expandtabs():", expanded_text) 

# find(): Finds the index of the first occurrence of a substring (returns -1 if not found)
index_of_mixed = text.find("MiXeD")
print("find('MiXeD'):", index_of_mixed)

# format(): Formats a string using positional or keyword arguments
#Alice goes in first one and then 3 goes into the other
formatted_text = "Hello, {}! You have {} new messages.".format("Alice", 3)
print("format():", formatted_text)

# format_map(): Similar to format(), but takes a dictionary for substitutions
data = {'name': 'Bob', 'messages': 5}
formatted_text_map = "Hello, {name}! You have {messages} new messages.".format_map(data)
print("format_map():", formatted_text_map) 

# index(): Similar to find(), but raises an error if the substring is not found
try:
    index_of_python = text.index("Python")  # This will raise ValueError
except ValueError:
    print("index('Python'): Substring not found!")

# isalnum(): Checks if all characters are alphanumeric (letters or digits)
is_alphanumeric = text.isalnum()
print("isalnum():", is_alphanumeric)  

# isdecimal(): Checks if all characters are decimal digits
is_decimal = "12345".isdecimal()
print("'12345'.isdecimal():", is_decimal)  

# isdigit(): Checks if all characters are digits (including some Unicode digits)
is_digit = "٢٣٤٥".isdigit()  # Arabic-Indic digits
print("'٢٣٤٥'.isdigit():", is_digit) 

# isidentifier(): Checks if the string is a valid Python identifier (variable name)
is_valid_identifier = "my_variable".isidentifier()
print("'my_variable'.isidentifier():", is_valid_identifier) 

# islower(): Checks if all cased characters are lowercase
is_lowercase = "hello".islower()
print("'hello'.islower():", is_lowercase) 

# isnumeric(): Checks if all characters are numeric (including Unicode numeric characters)
is_numeric = "½".isnumeric() 
print("'½'.isnumeric():", is_numeric)  

# isprintable(): Checks if all characters are printable (not control characters)
is_printable = text.isprintable()
print("isprintable():", is_printable)  

# isspace(): Checks if all characters are whitespace
is_whitespace = " \t\n".isspace()
print("' \t\n'.isspace():", is_whitespace)

# istitle(): Checks if the string is titlecased (first letter of each word capitalized)
is_titlecase = "This Is A Title".istitle()
print("'This Is A Title'.istitle():", is_titlecase) 

# isupper(): Checks if all cased characters are uppercase
is_uppercase = "HELLO".isupper()
print("'HELLO'.isupper():", is_uppercase) 

# join(): Joins elements of an iterable (e.g., a list) into a string using the given string as separator
words = ["Python", "is", "fun!"]
joined_string = " ".join(words)
print("join():", joined_string)  

# ljust(): Left-justifies the string within a given width, padding with a fill character (default is space)
left_justified = text.ljust(40, '.')
print("ljust():", left_justified) 

# lower(): Converts all characters to lowercase
lowercased_text = text.lower()
print("lower():", lowercased_text) 

# lstrip(): Removes leading characters (default is whitespace)
stripped_left = text.lstrip()
print("lstrip():", stripped_left) 

# partition(): Partitions the string into three parts based on a separator

#this is like a left partiftion by default

#It returns a tuple containing:

#The part of the string before the first occurrence of the separator.   
#The separator itself.   
#The part of the string after the first occurrence of the separator.   


partitioned_text = text.partition("-")
print("partition('-'):", partitioned_text)

# removeprefix(): Removes a prefix from the beginning of the string (if present)
prefix_removed = text.removeprefix("  ")
print("removeprefix('  '):", prefix_removed) 

# removesuffix(): Removes a suffix from the end of the string (if present)
suffix_removed = text.removesuffix(".  ")
print("removesuffix('.  '):", suffix_removed) 

# replace(): Replaces occurrences of a substring with another substring
replaced_text = text.replace(" ", "_")
print("replace(' ', '_'):", replaced_text) 

# rfind(): Finds the index of the last occurrence of a substring (returns -1 if not found)
last_index_of_s = text.rfind("s")
print("rfind('s'):", last_index_of_s)  

# rindex(): Similar to rfind(), but raises an error if the substring is not found
try:
    last_index_of_z = text.rindex("z")  # This will raise ValueError
except ValueError:
    print("rindex('z'): Substring not found!")

# rjust(): Right-justifies the string within a given width, padding with a fill character (default is space)
right_justified = text.rjust(40, '.')
print("rjust():", right_justified)

# rpartition(): Partitions the string into three parts based on a separator, searching from the right
#It returns a tuple containing:
#The part of the string before the first occurrence of the separator.   
#The separator itself.   
#The part of the string after the first occurrence of the separator.   

#Both partition() and rpartition() split the string into three parts based on the specified separator (in this case, a comma).
#partition() searches for the separator from the left side of the string and splits it at the first occurrence it finds.
#rpartition() searches for the separator from the right side of the string and splits it at the last occurrence it finds.

right_partitioned_text = text.rpartition(" ")
print("rpartition(' '):", right_partitioned_text) 

# rsplit(): Splits the string into a list from the right, using a separator (default is whitespace)
words_from_right = text.rsplit(maxsplit=2) 
print("rsplit(maxsplit=2):", words_from_right)

# rstrip(): Removes trailing characters (default is whitespace)
stripped_right = text.rstrip()
print("rstrip():", stripped_right) 

# split(): Splits the string into a list, using a separator (default is whitespace)
words = text.split()
print("split():", words)

# splitlines(): Splits the string into a list of lines

multiline_string = """This is a
multi-line string
with line breaks."""

lines = multiline_string.splitlines()
print("splitlines():", lines)

# startswith(): Checks if the string starts with a specified prefix
text = "Hello, world!"

# Check if the string starts with "Hello"
result1 = text.startswith("Hello")
print(result1)  # Output: True

# Check if the string starts with "world" (case-sensitive)
result2 = text.startswith("world")
print(result2)  # Output: False

# Check if the string starts with "world" within a specific range (from index 7 onwards)
result3 = text.startswith("world", 7)
print(result3)  # Output: True

# Check if the string starts with any of the prefixes in a tuple
prefixes = ("Hello", "Hi", "Greetings")
result4 = text.startswith(prefixes)
print(result4)  # Output: True (starts with "Hello")
