# Sid Bhatia
# CS 115-C
# Lecture 20 - Boolean Algebra

# Algebra With Only 0s and 1s!

## Real-valude variable --> variable must take any real number, e.g. x = 3.1234567
## Boolean variable --> a variable assigned to either 0 or 1, e.g. x = 0 or x = 1
### 0 and 1 are called "False" and "True" or "No" and "Yes" respectively

## Boolean algebra is founded upon George Boolean, 1815 - 1864

## Real Operators
### +
### - 
### x
### /
### ..

## Boolean Operators
### NOT --> 'not' in Python
### AND --> 'and' in Python
### OR --> 'or' in Python

# Fuctions

## Describing a real-valued function
### Words: f is a function of TWO real variables such that the output is the sum of their squares
### Table: x, y | f(x,y)
###        0  0 |   0
###        1  2 |   5
###       1.2 1 |   2.44
###        1  1 |   1

### It's difficult to completely describe a function using its table: it has so many real values.

### Formula: f(x,y) = x^2 + y^2

# Boolean Functions

## A Boolean function just takes Boolean arguments and gives a Boolean result
### e.g., f(True, True) = True

## The most common Boolean functions take 1 or 2 arguments (Uniary or Binary)
## There are exactly four 1-argument Booleans function; there are 16 2-argument functions, but only 5 are commonly used
## e.g., f(True) = True, f(False) = False, f(NOT True) = False, f(NOT False) = True

## Describing a Boolean function (inputs and outputs: 0 and 1)
### Words: f is a function of TWO binary (Boolean) variables such that the output is 1 *if and only if exactly one of the two inputs is 1*
### Table: x, y | f(x,y)
###        0  0 |   0
###        0  1 |   1
###        1  0 |   1
###        1  1 |   0

### The table works fine and is called a "truth table."