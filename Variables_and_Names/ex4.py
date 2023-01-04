# Assigned the cars variable an integer value of 100
cars = 100
# Assigned the space_in_a_car variable a floating point value of 4.0
space_in_a_car = 4.0
# Assigned the drivers variable an integer value of 30
drivers = 30
# Assigned the passengers variable an integer value of 90
passengers = 90
# Assigned the cars_not_driven variable equal to the cars variable minus the drivers variable
cars_not_driven = cars - drivers
# Assigned the cars_driven variable equal to the drivers variable
cars_driven = drivers
# Assigned the carpool_capacity variable equal to the cars_driven variable multiplied by the space_in_a_car variable
carpool_capacity = cars_driven * space_in_a_car
# Assigned the average_passengers_per_car variable equal to the passengers variable divided by the cars_driven variable
average_passengers_per_car = passengers / cars_driven


# Print the strings with the variables in between
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car")