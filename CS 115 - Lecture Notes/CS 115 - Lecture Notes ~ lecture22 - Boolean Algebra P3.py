# Sid Bhatia
# CS 115-C
# Lecture 22 -

## ANY Boolean function (no matter how complex) can ALWAYS be expressed
## using just AND OR NOT --> Minterm Expansion Principle
### You get an exponential number of terms: 2^(n) variables: Power Set?

## e.g., A function of TWO binary inputs x,y where the outputs
## is 1 iff x /neq y

# Properties of Boolean Functions

## All the 'usual' Boolean functions compute:
### f(x,y) = f(y,x) --> commutativity

### g(x,y) = "x <= y" --> not commutative
### x,y | g(x,y) | g(y,x)
### 0 0 |   1    |   1
### 0 1 |   1    |   0
### 1 0 |   0    |   1
### 1 1 |   1    |   1

## AND, OR, and XOR associative
### f(f(x,y), z) = f(x, f(y,z)) --> associativity
### e.g., (x AND y) AND z = x AND (y AND z)

### Table:  x | y | z |  xy  | (xy)z
###         0   0   0 |  0   |   0
###         0   0   1 |  0   |   0
###         0   1   0 |  0   |   0
###         1   0   0 |  0   |   0
###         0   1   1 |  0   |   0
###         1   0   1 |  0   |   0
###         1   1   0 |  1   |   0
###         1   1   1 |  1   |   1

# AND, OR, NOT is a "Universal Set"

## De Morgan's Laws:
### \bar[xy] = \bar[x] + \bar[y]
### \bar[x + y] = \bar[x]\bar[y]

#### Can have negation before or after the logic gate
#### Can have the negation of the negation to apply DeMorgan's Law 
#### (compliment of compliment cancels each other out)