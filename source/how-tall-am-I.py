'''
This is a demo application made by Micah Bredenhorst
This application is the second demonstration of the basic functionaltities of fuzzy logic.
This application will determine to what degree you are tall.
The application takes in the height of the user in centimeters (float) and returns the membership value (in what degree you are part of a certain set).
This is an value between 0 and 1, where 0 is not in the set and 1 is totaly being in the set.

The universe of discourse of the linguistic variable of heights are:
    - (very) Short
    - Average
    - (very) Tall

Example:
    - Input: 182.0
    - Output:
        You are 0.00 degree part of the set of very short
        You are 0.00 degree part of the set of short
        You are 0.30 degree part of the set of average
        You are 0.20 degree part of the set of tall
        You are 0.04 degree part of the set of very tall

Requirements:
    - matplotlib (pip)
    - fuzzylogic (pip)
'''

from matplotlib import pyplot
from fuzzylogic.classes import Domain
from fuzzylogic.functions import R, S, triangular
from fuzzylogic.hedges import very

plot = True
pyplot.rc("figure", figsize=(10, 10))

# Domain
height = Domain("Height", 140, 225, res=5)

# functions
height.short = S(160, 170)
height.very_short = very(height.short)
height.average = triangular(165, 185)
height.tall = R(180, 190)
height.very_tall = very(height.tall)

# User input
size = float(input("How tall are you in in centimeters?\n"))

print_membership = lambda membership, name: print("You are %.2f degree part of the set of %s" % (membership, name))
print_membership(height.very_short(size), "very short")
print_membership(height.short(size), "short")
print_membership(height.average(size), "average")
print_membership(height.tall(size), "tall")
print_membership(height.very_tall(size), "very tall")

# Plot
if plot:
    height.very_short.plot()
    height.short.plot()
    height.average.plot()
    height.tall.plot()
    height.very_tall.plot()
    pyplot.xlabel("Length in centimeters")
    pyplot.ylabel("Degrees of membership")
    pyplot.title("Plot of the fuzzy sets short, average and tall in the domain of height")
    pyplot.show()
