# File: hw3b.py
# Author: Sam Waggoner
# Date: 10/04/2020
# Section: 1006
# E-mail samuel.waggoner@maine.edu
# Description:
# We print out numbers descending from 101 to 1, and replace printing the number
# with a written statement if it meets certain parameters.
# Collaboration:
# I did not collaborate with anyone.

for i in range(101,0,-1):
    if (i) % 3 == 0 and (i) % 7 == 0 and (i) % 13 == 0:
        print("This should never happen!")
    elif (i) % 13 == 0 and (i) % 7 == 0:
        print("Lucky or unlucky?")
    elif (i) % 7 == 0 and (i) % 3 == 0:
        print("It's lucky to vote.")
    elif (i) % 3 == 0 and (i) % 13 == 0:
        print("It's unlucky to waste your time.")
    elif (i) % 3 == 0:
        print("Don't forget to vote on November 3rd.")
    elif (i) % 7 == 0:
        print("Seven games in an NBA final series.")
    elif (i) % 13 == 0:
        print("Thirteen original colonies.")
    else:
        print(i)