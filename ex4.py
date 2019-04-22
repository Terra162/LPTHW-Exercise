# Assigns 100 to the veriable cars
cars = 100
# Assigns 4 to space_in_a_car
space_in_a_car = 4
# Assigns 30 to drivers
drivers = 30
# Assigns 90 to passengers
passengers = 90
# cars_not_driven is assigned the value of cars - drivers
cars_not_driven = cars - drivers
# cars_driven is equal to the number of drivers
cars_driven = drivers
# carpool_capacity is equal to the cars_driven multiplied by the space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# the average_passengers_per_car is equal to passengers divided by cars_driven
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("we have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
