# Import argument variable from sys
from sys import argv

# Set the argv to accept two parameters, the script and a filename
script, filename = argv

# Prints the filename to be erased and the options for the following input
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# Prompts user for input
input("?")

# Prints the string and sets the target variable to the open file in 'write' ('w') mode
print("Opening the file...")
target = open(filename, 'w')

# Prints the following string and empties the file
print("Truncating the file. Goodbye!")
target.truncate()

# Prints the following string
print("Now I'm going to ask you for three lines.")

# Prompts the user for 3 inputs and sets the inputs to variables
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# Prints the following string
print("I'm going to write these to the file.")

# Writes the arguments to the file. "\n" character moves to the next line
target.write(f"{line1}\n{line2}\n{line3}")

# Prints the following string and closes the file
print("And finally, we close it.")
target.close()