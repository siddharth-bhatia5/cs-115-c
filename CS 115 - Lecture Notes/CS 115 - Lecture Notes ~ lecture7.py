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

# Range of list slicing: [starting index, ending index)

# To get halves of the list
first_half = print(lst2[:len(lst2)//2])
second_half = print(lst2[len(lst2)//2:])

# Everything regarding lists can be applied to strings
string = "Hello, world!"
print(string[0]) # string of length one, not character
print(string[0:5]) # string 'Hello'
print(string[:5]) # same concept because omit first index assumes starting at 0

# Can use negative indexing; counting from right uses negative #s
print(string[-1]) # string of '!'

# Third argument is the 'step'
print(string[0:len(string):2]) # skips every other character

# When you don't specify argument, step = '1'
print(string[::1])

# To reverse a string, use a negative steps
print(string[::-1]) # prints '!dlrow ,olleH'

# Slicing essentially runs a loop through the string/list
print(string[5:2:-1])

int_list = [0, 1, 2, 3, 4]

# double function
def double(x):
    return 2*x

print(double(2))

# map() function that setups up loop
# map(
doubles = list(map(double, int_list)) # list() casts input as a list
print(doubles)

# range() function like slicing
# range(start, stop, step)
# [inclusive, exclusive)
print(list(range(0, 1000, 10)))
