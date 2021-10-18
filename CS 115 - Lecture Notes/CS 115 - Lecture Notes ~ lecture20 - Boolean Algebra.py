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
###   0    0  0 |   0
###   1    0  1 |   1
###   2    1  0 |   1
###   3    1  1 |   0

### The table works fine and is called a "truth table."

# NOT, AND, OR

## Uniary Boolean function; NOT(x) outputs 1 if x is 0; written as bar(x) or x-bar
##  x | NOT x
##  0 |  1
##  1 |  0

## Binary Boolean function; AND(x,y) outputs 1 if x is 1 and y is 1 (both inputs are 1) [conjuncion]; written as xy
##  x, y | x AND y
##  0  0 |    0
##  0  1 |    0
##  1  0 |    0
##  1  1 |    1

## Multiplication refers to 'and'

## Binary Boolean function; OR(x,y) outputs 1 if either input is 1 (or both) [disjunction] and [inclusive OR]; written as x + y
##  x, y | x OR y
##  0  0 |    0
##  0  1 |    1
##  1  0 |    1
##  1  1 |    1

## 1 + 1 = 2, but, since you only have the option of 0 and 1, you represent it to be 1

# Playing with Functions

## Describe these functions in English:
### x x-bar --> x AND NOT x --> 1 if x is 1 and NOT x is 1 --> 1 if x is 1 and x is 0 --> never going to be 1 since it's impossible --> x\bar[x] = 0
#### Table:  x | x\bar[x]
####         0 |    0
####         1 |    0

### xx --> x AND x --> 1 if x is 1 and x is 1 --> 1 if x is 1
#### Table:  x | xx
####         0 | 0
####         1 | 1

### x + \bar[x] --> X OR NOT X --> 1 if x is 1 or NOT x is 1 --> 1 if x is 1 or x is 0 --> always going to be 1 \ x + x\bar[x] = 1
#### Table: x | x + \bar[x]
####        0 |     1
####        1 |     1

### xy + \bar[x]\bar[y] --> (x AND y) or (NOT x AND NOT y) --> 1 if (x is 1 and y is 1) or (x is 0 and x is 0) --> 1 if both are the same (0 0 or 1 1)
#### Table: x, y | xy + \bar[x]\bar[y]
####        0  0 |          1
####        0  1 |          0
####        1  0 |          0
####        1  1 |          1