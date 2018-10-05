#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 08:44:35 2018

@author: denisvrdoljak
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 08:27:49 2018

@author: denisvrdoljak
"""

# Simple while loop
barn = ['cat','dog','elephant','giraffe']
i=0
# i is a counter that will help us iterate through the list
# when i gets to the end of the list, the loop will stop
while i < len(barn):
    print(barn[i] + " found in the barn")
    i += 1
    #increment counter


# Simple while loop
barn = ['cat','dog','elephant','giraffe','pig']
i=0
# i is a counter that will help us iterate through the list
# when i gets to the end of the list, the loop will stop
while i < len(barn):
    print(barn[i] + " found in the barn")
    i += 1
    #increment counter

print("\n\n")
# print out some white space

# While loop with if statement
barn = ['cat','dog','elephant','giraffe','pig']
i=0
# i is a counter that will help us iterate through the list
# when i gets to the end of the list, the loop will stop
while i < len(barn):
    print(barn[i] + " found in the barn")
    if len(barn[i]) > 3:
        print("\tThat's a big "+barn[i]+"!")
    i += 1
    #increment counter

print("\n\n")
# print out some white space


# While loop with if, break
barn = ['cat','dog','elephant','giraffe','pig']
i=0
# i is a counter that will help us iterate through the list
# when i gets to the end of the list, the loop will stop
while i < len(barn):
    print(barn[i] + " found in the barn")
    if len(barn[i]) > 3:
        print("\tThat's a big "+barn[i]+"! It won't fit in a barn...let's just stop (break) here.")
        break
    i += 1
    #increment counter




print("\n\n")
# print out some white space

# Simple WHILE loop
barn = ['cat','dog','elephant','giraffe','pig']
i=0
# i is a counter that will help us iterate through the list
# when i gets to the end of the list, the loop will stop
while i < len(barn):
    animal = barn[i]
    print(animal + " found in the barn")
    i += 1
    #increment counter

print("\n\n")
# print out some white space

# Simple FOR loop
barn = ['cat','dog','elephant','giraffe','pig']
i=0
# i is a counter that will help us iterate through the list
# when i gets to the end of the list, the loop will stop
barn = ['cat','dog','elephant','giraffe','pig']
for animal in barn:
    print(animal + " found in the barn")

print("\n\n")
# print out some white space


for letter in "animal":
    print(letter)
    
    
    