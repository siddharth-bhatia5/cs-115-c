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

### Step #1:
#### Create the truth table

### Step #2:
#### Focus on the rows with 1

### Step #3:
#### Have to do conjunction of all variables (AND); order doesn't matter bceause it commutative at the end
#### You're seeing ****WHICH IS THE PRODUCT OF ALL ONES TO GIVE THE RESULTANT ONE****

### Step #4:
#### Any function can be viewed as the superimposition of those minterms, so disjunction of all minterms

### AND, OR, NOT --> can be described as any combination of AND, ORs, NOTs

# Digital Logic Gates
## Final goal is to get hardware to care it out with logic gates

### NOT is viewed as a small circle or 'bubble' on another gate
### The gate is viewed a signal coming in and a signal goes out

#### Flat side = input side; curved/smooth side = output side for AND
#### Curved side = input side; pointed side = output side for OR

#### AND: flat --> curved
#### OR: curved --> pointed

#### Symbols for each operation --> gates for each operations

#### when variable is used multiple times, it splits in circuit digram with a *wire*

#### Advantage of circuit diagrams removes any knowledge of precedence --> easiest for hardware
#### Hardest description of function --> take it down to a concrete level with diagrams