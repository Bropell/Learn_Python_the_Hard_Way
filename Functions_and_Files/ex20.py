# Import dependencies
from sys import argv

# Set the argv to accept two parameters: script and input_file
script, input_file = argv

# Define print_all function to accept one argument
# Function reads the input file and prints to the console
def print_all(f):
    print(f.read())

# Define rewind function to accept one argument
# Function sets the reference point to the beginning of the file
def rewind(f):
    f.seek(0)

# Define print_a_line function to accept two arguments
# Function prints out the line count and the contents of that line
def print_a_line(line_count, f):
    print(line_count, f.readline(), end = "")

# Sets the current_file variable equal to the opened input file 
current_file = open(input_file)

# Prints the following string
print("First let's print the whole file:\n")

# Calls the print_all function passing the current_file variable as the argument
# This prints the file contents
print_all(current_file)

# Prints the following string
print("Now let's rewind, kind of like a tape.")

# Calls the rewind function passing the current_file variable as the argument
# Sets the reference point to the beginning of the file
rewind(current_file)

# Prints the following string
print("Let's print three lines:")

# Sets the current_line variable equal to 1
current_line = 1 
# Calls the print_a_line function passing the current_line and current_file variables as arguments
# Prints the current line, which is 1 here, and the contents of line 1
print_a_line(current_line, current_file)

# Increments the current_line variable by 1
current_line += 1
# Calls the print_a_line function passing the current_line and current_file variables as arguments again
# Prints the current line, which is 2 here, and the contents of line 2
print_a_line(current_line, current_file)

# Increments the current_line variable by 1
current_line +=1
# Calls the print_a_line function passing the current_line and current_file variables as arguments again
# Prints the current line, which is 3 here, and the contents of line 3
print_a_line(current_line, current_file)