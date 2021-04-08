# File: hw3c.py
# Author: Sam Waggoner
# Date: 10/04/2020
# Section: 1006
# E-mail samuel.waggoner@maine.edu
# Description:
# We print out a list and write the number of the list next to the color in the list.
# Collaboration:
# I did not collaborate with anyone.

colors = ["red","yellow","green","brown","scarlet","black","ochre","peach","ruby"]
print("The color list is:")
for i in range(0,(len(colors))):
    print((i+1),": ", colors[i], sep="")
print("So many colors!")