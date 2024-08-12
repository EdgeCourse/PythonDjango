#does not find
#print(__doc__) 

def calculate_area(length, width):
  """
  does not work if __doc__ printed above
  
  does not work if assigned to variable 
   
  press q to quit
  
  This function calculates the area of a rectangle.

  Args:
      length: The length of the rectangle.
      width: The width of the rectangle.

  Returns:
      The calculated area of the rectangle.
  """
  area = length * width
  return area

# Access the docstring using the __doc__ attribute
print(calculate_area.__doc__)

# Use the help() function to view the docstring and other information
help(calculate_area)

