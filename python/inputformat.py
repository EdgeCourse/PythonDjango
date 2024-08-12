#suppress newline for user input
name = input("Enter your name: ")  # Default behavior, newline after input
print("Hello,", name)

age = input("Enter your age: ", end="")  # No newline, prompt and input on the same line
print("! You are", age, "years old.")

####
#progress bar
import time

for i in range(1, 11):
    print("#" * i, end="")  # Print progress bar, no newline
    time.sleep(0.5)  # Simulate some work
print("\nDone!")  # Print "Done!" on a new line after the loop

####
#build a file path
base_dir = "C:\\Users\\Documents"
folder_name = "project"
filename = "report.txt"

file_path = base_dir, folder_name, filename  # Create a tuple of path components
print(*file_path, sep="\\")  # Join components with backslashes as separators
