# Import dependencies
from sys import argv
from os.path import exists

# Set the argv to accept three parameters: the script, a from_file and a to_file
script, from_file, to_file = argv

# Print the following string with variables from_file and to_file inserted
print(f"Copying from {from_file} to {to_file}")

# Set the variable 'in_file' equal to from_file opened
in_file = open(from_file)
# Set the variable 'indata' equal to 'in_file' variable read
indata = in_file.read()

# Prints the following string with the length of the indata variable inserted
print(f"The input file is {len(indata)} bytes long")

# Prints the following strings and tells the user whether the 'to_file' exists
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
# Prompt the user for input
input()

# Sets the 'out_file' variable equal to 'to_file' opened in 'write' mode.
out_file = open(to_file, 'w')
# Writes the contents of 'indata' to out_file
out_file.write(indata)

# Prints the following string
print("Alright, all done.")

# Closes the files
out_file.close()
in_file.close()