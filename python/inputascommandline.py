import sys

"""
#make sure there are the right number of command line arguments
if len(sys.argv) != 4:
    print("Usage: python script_name.py <your_name> <your_quest> <number>")
    sys.exit(1)  # Indicate an error
"""    

user_name = sys.argv[1]
quest = sys.argv[2]
num = float(sys.argv[3])

"""
#or, make sure this argument (by position) is a number, replace num assignment with:
try:
    num = float(sys.argv[3])
except ValueError:
    print("Invalid number. Please provide a valid number.")
    sys.exit(1)
"""

print(f"{user_name} seeks {quest}")
print(f"2 times {num} is {num * 2}")
