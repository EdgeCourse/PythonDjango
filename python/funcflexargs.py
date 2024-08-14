"""
    **kwargs

Captures any additional keyword arguments (arguments passed with their names) that are not explicitly defined in the function's parameter list.
Creates a dictionary where the keys are the keyword argument names, and the values are the corresponding argument values.
Allows you to pass an arbitrary number of keyword arguments to a function, making it more adaptable to varying inputs.
"""

def my_function(arg1, arg2, **kwargs):
    print(f"arg1: {arg1}, arg2: {arg2}")
    print("kwargs:", kwargs)

my_function(1, 2, name="Alice", age=30)

"""
    *

Captures any additional positional arguments (arguments passed without their names) that are not explicitly defined in the function's parameter list.
Creates a tuple containing the extra positional arguments.
Allows you to pass a variable number of positional arguments to a function.
"""

def my_function(arg1, *args):
    print(f"arg1: {arg1}")
    print("args:", args)

my_function(1, 2, 3, 4)

"""
/

Forces all parameters preceding it to be positional-only. This means they can only be passed by their position in the function call, not by their keyword.
Enhances code readability by making it clear which parameters are intended to be positional-only.
Useful when you want to ensure compatibility with older versions of Python or when you're designing APIs where parameter names might change in the future.

"""

def my_function(arg1, /, arg2, arg3):
    print(f"arg1: {arg1}, arg2: {arg2}, arg3: {arg3}")

my_function(1, 2, 3)  # Valid
my_function(arg1=1, arg2=2, arg3=3)  # Invalid, arg1 is positional-only

"""
    positional only: add * before args
"""
    
def my_function(*, x):
  print(x)

my_function(x = 3)

"""
You can combine the two argument types in the same function.

Any argument before the / , are positional-only, and any argument after the *, are keyword-only.

"""
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)