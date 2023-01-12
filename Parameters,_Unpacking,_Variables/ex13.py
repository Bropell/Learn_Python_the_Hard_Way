# Import argv from sys module
from sys import argv

# Sets argv to the script and three other arguments 
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)