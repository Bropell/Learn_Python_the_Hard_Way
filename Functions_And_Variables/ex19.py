# Define function cheese_and_crackers to take two arguments
# Function executes the four print statements inserting the arguments and ends with a newline character
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# Print the following string
print("We can just give the function numbers directly:")
# Calls the cheese_and_crackers function with numbers as arguments
cheese_and_crackers(20, 30)

# Prints the following string
print("OR, we can use variables from our script:")
# Defines two variables and sets them equal to numerical values
amount_of_cheese = 10
amount_of_crackers = 50

# Calls the cheese_and_crackers function with variables as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Prints the following string
print("We can even do math inside too:")
# Calls the cheese_and_crackers function using numbers and math as arguments
cheese_and_crackers(10 + 20, 5 + 6)

# Prints the following string
print("And we can combine the two, variables and math:")
# Calls the cheese_and_crackers function using variables and math as arguments 
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)