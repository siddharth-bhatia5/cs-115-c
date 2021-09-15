# CS 115-C
# Sid Bhatia
# Lecture #7 - Notes ~ Programming with Lists

# Programming with Lists:
## Indexing
## Slicing
## Updating a List
## Testing for Emptiness
## len()
## List Arithmetic
## range()
### list()
## filter()
## map()
## functions.reduce

lst = [1,2,3,4] # define a list using bracket '[]' syntax

# To access elements of a list, use indexing or subscripting
num = lst[2]
print(lst[2])

# In computer science, you start counting at 0
# List goes from [0, len(lst) - 1]

# Therefore, lst[4] would give 'IndexError: list index out of range'

# Can change the value of the elements: lists are mutable
lst[2] = 9
print(lst[2])

# Python has no arrays, only lists
others = ['a','b', 'c'] # there's no difference between characters & strings

print(lst + others) # concatenates or combines the two lists

# Python is dynmaically typed, so it doesn't care if you make a list with
# multiple things; lists can contain multiple types of variables

lst2 = lst + others
yal = [lst2, lst, 'Hello', 'World'] # lists can contain lists, aka heterogenous lists
print(yal)

length = len(yal) # returns the number of elements in the list
print(length)

other2 = [] # empty list, len(other2) = 0

# slicing = way to take a sub-category/subsequence (substring, sublist, etc.)
# [index of first position you want to start : index you want to end at (exclusive)]
print(lst2[2:5])

# To go to end of list, omit last index (assumes last index = length of list)
print(lst2[2:])

