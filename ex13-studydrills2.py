#!/usr/bin/env python3.6

# ex13: Parameters, Unpacking, Variables
# Write a script that has more arguments.

from sys import argv

script, name, age, height, weight = argv

print("The script is called:", script)
print("Your name is:", name)
print("Your age is:", age)
print("Your height is %d cm" % int(height))
print("Your weight is %d kg" % int(weight))
