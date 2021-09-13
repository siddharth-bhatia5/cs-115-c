# CS 115-C
# Sid Bhatia
# Lecture #5 - Notes

# Operator "/" is different from "//"
# The operator "/" returns a float
# Two main categories of numbers: integer numbers & floating point numbers

# Division opeator is between two floating point numbers (decimals)
print(4 / 4) # e.g., prints 1.0

# Python is not a typed language; you don't need to specify the type
# of your variables (in contrast to languages like Java)
num1 = 10
num2 = 5

# Double slash = integer division
print(num1 // num2) # e.g., prints 2


# Integral division
# Quotient = dividend // divisor
print(7/3) # prints 2.333 repeating
print(7//3) # prints 2

# Remainder/modulo operator (mod)
# Dividend = quotient * divisor + remainder
# Remainder = dividend - quotient * divisor
# a = q*b + 4
# q = a//b
# r = a = q*b
# r = a % b
# r = a - (a//b) * b
print(7 % 3) # e.g., 7 "mod" 3 = 1

# Following are known as "statements," meaning they don't show the result
a = 7
b = 3
q = a//b
print(q) # Printing the variable shows the result

# REPL
# Read Evaluate Print Loop

# you're assigning y the output of the print, which is nothing
# the return value of the "print" function is void
y = print(4 / 2) # prints 2 but y = nothing

# convert 37 Celsius to Fahrenheit
# Celsius
# Freezing: 0
# Scale: 100
# Fahrenheit
# Freezing: 32
# Boiling: 212
# Scale: 180

cel = 37
print(cel)

# You tell what your program is going to do by using a docstring
# You signify the docstring by using triple double quotes: """
# You can also use triple single quotes: '''
def convert_celsius_to_fahrenheit(c):
    """
    Function that converts degrees in Celsius to Fahrenehit.
    """
    return c*(9/5) + 32

print(convert_celsius_to_fahrenheit(cel))

# To define a function, you use the "def" keyword
# Following "def" is the function name
# Something going in = parameter
# Something going out = output
# Name descriptive variables and parameters

def to_F(degree_C):
    return degree_C * (9/5) + 32 # No output because told Python what to do with this function

to_F # If you don't specify an argument,
# it will show the memory location of the function in the shell

# When you invoke or call the function,
# you provide an input which is an argument.
# The argument is in parentheses.
print(to_F(37))

# Don't write code in a shell; write it in the IDLE

# "import" keyword retrieves the library known as "math"
# The "math" library contains a myriad of functions concerning math
import math

# The "from" keyword allows you to skip calling "math" for each function
# in the math libary

from math import sqrt
