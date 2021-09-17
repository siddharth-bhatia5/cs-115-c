# Sid Bhatia
# CS-115
# Lecture #8 - Map and Reduce

import math

s = 'HELLO'
list(s) # converts string 's' into a list of single characters
print(list(s))

# converts character or number to ASCII
print(ord('A')) # prints 65
print(chr(76)) # prints 'L'

# ASCII maps characters continously
# 'A' = 65 and 'B' = 65
# 'A' - 'Z' are successive code-points

def encode_char(c, off):
    # chr(ord(C) + off...)
    return null

# when you encode and decode, you should get the same answer

# range is similar to slicing with start, stop, and step
# one argument --> defaults stop to 0 and step to 1

print(list(range(10))) # prints a list of the first 10 numbers, excluding 10

print(range(100, 110)) # returns range object

list(range(100, 110)) # gives 100-109

list(range(100, 110, 3))

def get_evens(bound):
    """
    Outputs a list of even numbers starting at 0
    and up to but not including the bound.
    """
    # need to have three arguments to set the step
    return list(range(0, bound, 2)) 

print(get_evens(100))

print()

def get_odds(bound):
    """
    Outputs a list of odd numbers starting at 1
    and up to but not including the bound.
    """
    # need to have three arguments to set the step
    return list(range(1, bound, 2)) 
    
print(get_odds(100))

print()

# can't get the square of numbers using range; you need the map questions

def double_num(x):
    return x*2

def get_evens_via_map(bound):
    int_range = range(bound // 2) # start with half of the list
    evens = list(map(double_num, int_range))
    return evens

print(get_evens_via_map(100))

get_evens_via_map(10)
# first computes range object of [0, 1, 2, 3, 4]
# next, it computes a map object of [double_num(0), double_num(1), double_num(2)...]

# the map() function applies a function to an iterable

def square_num(x):
    return math.pow(x,2)

def get_squares_via_map(bound):
    # ceil() function rounds up to next integer
    int_range = range(math.ceil(math.sqrt(bound))) # changes bound to number of squares
    squares = map(square_num, int_range)
    return list(squares) # better style


print(math.ceil(math.sqrt(70))) # prints 9
print(get_squares_via_map(100))

def get_averages(list1, list2):
    """
    Gets the averages of the homeworks for three students.
    """
    # list1 = [9,8,10], list2 = [9,10,7]
    # ouput: [9, 9, 8]
    def avg(x,y):
        """
        Helper innner function that takes the average of two values.
        """
        return (x+y) // 2
    avg_grades = map(avg, list1, list2)
    return list(avg_grades)

print(get_averages([9,8,10],[9,10,7]))

# map converts list into a list

from functools import reduce
# factorial(n) = 1*2*3*4*n
# factorial(6):
# [1, 2, 3, 4, 5, 6, ... n]

# output is a single value: multiple each value
# [1*2, 3, 4, 5, 6] --> reduces the list by 1 by multiplying the list by 2
# [2*3, 4, 5, 6]
# [6*4, 5, 6]
# [24*5, 6]
# [120*6]
# 720

def multiply(x,y):
    return x * y

def factorial_via_reduce(n):
    int_range = list(range(1, n+1))
    return reduce(multiply, int_range)

print(factorial_via_reduce(6))

def overall_avg_grade(list1, list2):
    avg_list = get_avg_list(list1, list2)
    def add(x,y):
        return x + y
    overall_sum = reduce(add, avg_list)
    return overall_sum // len(avg_list)

print(sum(range(10))) # summates the first 10 numbers
