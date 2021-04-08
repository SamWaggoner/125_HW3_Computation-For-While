# File: hw3d.py
# Author: Sam Waggoner
# Date: 10/04/2020
# Section: 1006
# E-mail samuel.waggoner@maine.edu
# Description:
# Using nested while loops we ask for names and numbers under that name until
# encountering sentinels -1 and q.
# Collaboration:
# I went to Matt's Boardman office hours Monday for help. He introduced me to
# using + instead of commas (for too many inputs) and helped me fix my code.
# He's very nice and helpful, I'm very glad I stopped in!


name = input("What is your name? " )
num = -99999999999999999999999999999999999999999999999999999
highestnum = -99999999999999999999999999999999999999999999999999999
while name != "q":
    while num != -1:
        num = int(input("Hi, " + name + ", please enter a number: "))
        if num > highestnum:
            highestnum = num
    print("Your highest number is " + str(highestnum))
    num = -99999999999999999999999999999999999999999999999999999
    highestnum = 0
    name = input("What is your name? ")
print("Goodbye")

# I first attempted to use a list when storing the numbers. When I went to
# Matt's office hours, he wrote this code. I'm putting it here just for
# future reference as a different sort of solution.

"""        
name = input("What is your name? ")
while name != 'q':
    listNums = []
    num = int(input("Please enter a number: "))
    while num != -1:
        listNums.append(num)
        for i in range(len(listNums)):
            if i == 0:
                highest = listNums[i]
            elif listNums[i] > highest:
                highest = listNums[i]
        num = int(input("enter a num: "))
    print(highest)
    name = input("enter your name: ")
print("goodbye")
"""