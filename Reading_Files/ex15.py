# Import argument variable from sys
from sys import argv

# Set the argv to accept two parameters, the script and a filename
script, filename = argv

# Set txt variable equal to the file that was opened 
txt = open(filename)

# Print the formatted string with the value of filename. Then call the .read function on txt to print the contents
print(f"Here's your file {filename}:")
print(txt.read())

# Close file when done
txt.close()

# Prints a string. Then prompts the user for input and sets the input to the file_again variable
print("Type the filename again:")
file_again = input("> ")

# Set txt_again variable equal to opened variable (which should be a file) 
txt_again = open(file_again)

# Prints the contents of txt_again variable after calling .read function on it
print(txt_again.read())

# Close file when done
txt_again.close()