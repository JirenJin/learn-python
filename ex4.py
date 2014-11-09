# define the number of cars
cars = 100
# define the space of each car
space_in_a_car = 4.0
# define the number of drivers
drivers = 30
# define the number of passengers
passengers = 90
# compute the number of cars without drivers
cars_not_driven = cars - drivers
# assign the number of cars with drivers with the number of drivers 
cars_driven = drivers
# compute the capacity of carpool
carpool_capacity = cars_driven * space_in_a_car
# compute the average of passengers in each car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
print "Hey %s there." % "you"
