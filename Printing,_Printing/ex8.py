# Assign the formatter variable to the string value "{} {} {} {}"
formatter = "{} {} {} {}"

# Prints the formatter variable as a string with the arguments 1, 2, 3 ,4 in the four {}'s
print(formatter.format(1, 2, 3, 4))

# Prints the formatter variable as a string with the arguments "one", "two", "three", "four" in the four {}'s
print(formatter.format("one", "two", "three", "four"))

# Prints the formatter variable as a string with the arguments True, False, False, True in the four {}'s
print(formatter.format(True, False, False, True))

# Prints the formatter variable as a string with the arguments formatter, formatter, formatter, formatter in the four {}'s
print(formatter.format(formatter, formatter, formatter, formatter))

# Prints the formatter variable as a string with the arguments "Try your", "Own text here", "Maybe a poem", "Or a song about fear" 
# in the four {}'s
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))