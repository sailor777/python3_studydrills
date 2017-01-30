#!/usr/bin/env python3

# ex5: More Variables and Printing

name = 'Zed A. Shaw'
age = 36      # not a lie
height = 172  # cm
weight = 60  # kg
eyes = "Green"
teeth = 'White'
hair = 'Red'

print("Let's talk about %s" % name)
print("He's %d centimeters tall." % height)
print("He\'s %d kilogram heavy." % weight)
print("He's got %s eyes and %s hair." % (eyes, hair))
print("Actually that's not too heavy")
print("His teeth are usually %s depending on the coffee." % teeth)

# this line is tricky, try to get it exactly right
print('If I add %d, %d and %d I get %d.' % (age, height, weight, age + height + weight))

# try more format characters
greeting = "Hello,\t"
first_name = 'Danko'
last_name = 'Yanko'
age = 22
# Print 'Hello,\t'my name is Joseph Pan, and I'm 24 years old.
print("%r my name is %s %s, and I'm %d years old." % (greeting, first_name, last_name, age))

# Try to write some variables that convert the inches and pounds to centimeters and kilos.
inches_per_centimeters = 2.54
pounds_per_kilo = 0.45359237

print("He's %f inches tall." % (height / inches_per_centimeters))
print("He's %f pounds heavy." % (weight / pounds_per_kilo))
