## Skill Drill was to shorten the ex17.py script as much as possible and make it more friendly by removing unnecessary features.

# Import dependencies
from sys import argv

# Set the argv to accept three parameters: the script, a from_file and a to_file
script, from_file, to_file = argv

# Print the following string with variables from_file and to_file inserted
print(f"Copying from {from_file} to {to_file}")

# Sets the 'out_file' variable equal to 'to_file' opened in 'write' mode.
# Write the opened from_file data, after it's read, to the to_file
out_file = open(to_file, 'w').write(open(from_file).read())

# Prints the following string
print("Alright, all done.")