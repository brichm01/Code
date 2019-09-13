# Learn Python the Hard Way Exercise 4
# Bill Richmond
# v1 2019-09-13
# Set the number of cars
cars = 100
# Set the seating capacity for a car
space_in_a_car = 4
# Set the number of drivers available
drivers = 30
# Set the number of passengers
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
