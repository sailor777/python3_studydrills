#!/usr/bin/env python3.6

# ex8: Printing, Printing

formatter = "%s %s %s %s"

print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",  # This line contains a apostrophe
    "So I said goodnight."
    ))
