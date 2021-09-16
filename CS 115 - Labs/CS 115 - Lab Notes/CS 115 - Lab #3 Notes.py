# Sid Bhatia
# CS 115-C
# Lab #3 - Notes

lst = [1,2,3,4,5,6,7,8,9]

def add_one(x):
    return x + 1

print(add_one(1))

print(list(map(add_one, lst))) # have to use list(...) when using map

# map returns a map object or a list
# map is built-in function

# you have to import reduce since it's not built-in

from functools import reduce

def add(x,y):
    return x + y

# reduce returns a value, not a map object

print(reduce(add, lst)) # summates the numbers in the list

