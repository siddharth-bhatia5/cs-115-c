# Sid Bhatia
# CS 115-C
# Lecture 22 -

## ANY Boolean function (no matter how complex) can ALWAYS be expressed
## using just AND OR NOT --> Minterm Expansion Principle
### You get an exponential number of terms: 2^(n) variables: Power Set?

## e.g., A function of TWO binary inputs x,y where the outputs
## is 1 iff x /neq y

## Table:    x,y | f(x,y)
##           0 0 |   0



# AND, OR, NOT is a "Universal Set"
## \bar[x]\bar[y] = \bar[x] + \bar[y]
## \bar[x + y] = \bar[x]\bar[y]

# Properties of Boolean Functions

## All the 'usual' Boolean functions compute:
### f(x,y) = f(y,x) --> commutativity

## AND, OR, and XOR associative
### f(f(x,y), z) = f(x, f(y,z)) --> associativity
### e.g., (x AND y) AND z = x AND (y AND z)