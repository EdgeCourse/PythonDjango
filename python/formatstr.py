#f-strings were introduce in Ptyhon 3.6

#insert variables
name = "Alice"
age = 30

greeting = f"Hello, {name}! You are {age} years old."
print(greeting)  # Output: Hello, Alice! You are 30 years old.

#insert expressions
x = 10
y = 3

result = f"The sum of {x} and {y} is {x + y}."
print(result)  # Output: The sum of 10 and 3 is 13.

#format numbers
pi = 3.14159

formatted_pi = f"Pi is approximately {pi:.2f}"  # Format to 2 decimal places
print(formatted_pi)  # Output: Pi is approximately 3.14

#multiline
name = "Bob"
city = "New York"

info = f"""
Name: {name}
City: {city}
"""

print(info)

#call a function in f-string
def get_current_time():
    import datetime
    return datetime.datetime.now().strftime("%H:%M:%S")

time_message = f"The current time is: {get_current_time()}"
print(time_message)  # Output: The current time is: 12:41:19 (or similar, depending on the actual time)

"""f-strings: preferred choice for most modern Python code due to their readability, conciseness, and performance.

str.format(): good alternative for more control over formatting options or are working with older Python versions that don't support f-strings.

% operator: used in legacy code or when interfacing with C-style libraries. 

Template strings: simple substitutions, especially when security is a concern (helps prevent code injection vulnerabilities).
"""



#ALTERNATIVES
#format method - common

name = "Bob"
age = 25
greeting = "Hello, {}! You are {} years old.".format(name, age)
print(greeting)  # Output: Hello, Bob! You are 25 years old.

#old-style %
name = "Charlie"
age = 35
greeting = "Hello, %s! You are %d years old." % (name, age)
print(greeting)  # Output: Hello, Charlie! You are 35 years old.

#Template Strings (string.Template)
#Useful for simple variable substitutions, 
#uses $ followed by the variable name within the string.
# Values are passed as a dictionary to the substitute() method.

from string import Template

template = Template("Hello, $name! You are $age years old.")
values = {'name': 'David', 'age': 40}
greeting = template.substitute(values)
print(greeting)  # Output: Hello, David! You are 40 years old.

