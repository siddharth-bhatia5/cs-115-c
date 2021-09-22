############################################################
# CS115 Lab 4
# Name: Sid Bhatia
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
############################################################

from functools import reduce
import math

# Task 1: Use reduce to add up all elements in a list
"""
Input: A list of numbers
Output A number representing the sum
Example: add_all([1, 2, 3]) = 6
"""
def add_all(lst):
    def add(x, y):
        return x + y
    return reduce(add, lst)

# print(add_all([1,2,3]))
# print(add_all([10,20,30]))

# Task 2: Use map to evaluate a given polynomial at a specific x-value
"""
Input:
  p: A list of coefficients for increasing powers of x
  x: The value of x to evaluate
Output: Number representing the value of the evaluated polynomial
Example: poly_eval([1, 2, 3], 2) = 1(2)^0 + 2(2)^1 + 3(2)^2 = 17
"""
def poly_eval(p, x):

    if len(p) == 0: # null list
        return p

    # if there are three coefficients, it's a 2nd degree polynomial
    num_of_terms = len(p)
    powers = range(0, num_of_terms) # list of number of powers
    
    def add(a,b):
        return a + b            
    def mult(a,b):
        return a * b            
    # Returns the value of x to the ith power
    def x_powers(i):            
        return x ** i
    
    # could involve range() function
    # reduce on the outside

    # take each value to it's power
    # multiply by it's coefficient
    # add them together
    # return it
    
    powers_list = list(map(x_powers, powers)) # gives list of values to the power
    multi_list = list(map(mult, p, powers_list)) # gives multiplied list
    value = reduce(add, multi_list) # gives the final value
    
    return value

# Test Cases:

# print(range(3))

# print(poly_eval([1,2,3], 2))
# print(poly_eval([1,2,3,4,5], 2))
# print(poly_eval([],2))
# print(poly_eval([1,2,3], 3))
