# Assigned the types_of_people variable an integer value of 10
types_of_people = 10
# Assigned the variable x to a string with the types_of_people variable within it 
x = f"There are {types_of_people} types of people."

# Assigned the binary variable to the string "binary"
binary = "binary"
# Assigned the do_not variable to the string "don't"
do_not = "don't"
# Assigned the variable y to a string with the binary and do_not variables within it
y = f"Those who know {binary} and those who {do_not}."

# Prints the values of x and y respectively
print(x)
print(y)

# Print string with the x variable within it
print(f"I said: {x}")
# Print string with the y variable as a string within it
print(f"I also said: '{y}'")

# Assign the hilarious variable to the Boolean value of False
hilarious = False
# Assign the joke_evaluation variable to the string "Isn't that joke so funny?! with an empty value at the end
joke_evaluation = "Isn't that joke so funny?! {}"

# Prints joke_evaluation with the value of hilarious formatted  
print(joke_evaluation.format(hilarious))

# Assign the variable w to the string "This is the left side of..."
w = "This is the left side of..."
# Assign the variable e to the string "a string with a right side."
e = "a string with a right side."

# Prints the addition of the two string variables as a longer string
print(w + e)