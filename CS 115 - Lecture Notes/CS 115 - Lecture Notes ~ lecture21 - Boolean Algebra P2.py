# Sid Bhatia
# CS 115-C
# Lecture 21 - Boolean Algebra P2

# Playing with Functions

## Boolean Formulae for:

### A function of two variables x,y that evaluates to 1 iff x and y are not equal
#### (x\bar[y] + \bar[x]y) --> (x AND (NOT y)) or (NOT x and y)

### Go from expression in English to truth table and reverse engineer to Boolean expression

#### Step #1
#### Truth Table:   x, y | 
####                0, 0 |  0     
####                0, 1 |  1
####                1, 0 |  1
####                1, 1 |  0

### Step #2                                                         
#### Derived Truth Table:   x, y | \bar[x], \bar[y] | x\bar[y] | \bar[x]y | x\bar[y] + \bar[x]y
####                        0  0 |    1      1      |    0     |    0     |          0
####                        0  1 |    1      0      |    0     |    1     |          1
####                        1  0 |    0      1      |    1     |    0     |          1
####                        1  1 |    0      0      |    0     |    0     |          0

## Minterm Expansion Principle:
### Minterm = smallest expression you can write that is equivalent to an entry in the table

### Once you have the truth table, focus only on the rows with 1
### e.g., can you get an expression that gets 0 1 0 0? can you get an expression that gets 0 0 1 0?
### If so, once you have those expressions, you can superimpose them by using an 'OR' operator or '+': 0 1 1 0
### therefore, f(x,y) = \bar[x]y + x\bar[y] = x XOR y

#### Build an expression by doing the 'OR' of a bunch of terms which have only a row with '1'
#### If your row has a 0 with that variable, then the term in your midterm is 'NOT' or negation of variable
#### If your row has a 1 with that variable, then the variable shows up positive

