def greet(name):
    """
    This function greets a person by name.

    Args:
        name: The name of the person to greet.
    """
    print(f"Hello, {name}!")

# Using __doc__
print(greet.__doc__)  

# Using help()
help(greet)
