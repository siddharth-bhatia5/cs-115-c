# Sid Bhatia
# CS 115-C
# Lecture #19 - Binary Subtraction & Negative Numbers

# Midterm Q1, Q2, Q3, Q4, Q5
# Each question should be 5 - 10 minutes
# Start each question one-by-one
# You can use the study sheet (you submit it Thursday night/8 AM Friday morning)
# No negative numbers in Binary

# Binary: decimal --> binary; binary --> decimal; addition
# Binary multiplication: Russian Peasants

## Not on midterm:
### Binary subtraction
### Negative numbers
### Adding the negated second term

## Binary subtraction:

# Comma has no meaning but to separate the number of bits in four
#   (0110,1001)_2 - (0100,0111)_2 == ?
# 8 bits = 1 byte; 4 bits = 1 nibble/hex digit

# break up the 8 bits into two 4 bit sub-groups to make it easier to compute

#   0 1 1 0    1 0 0 1 --> (105)_10
# - 0 1 0 0    0 1 1 1 --> (71)_10
# --------------------
# 1 1 1 1 1        1 --> carry on numbers
#   0 1 1 0    1 0 0 1
# + 1 0 1 1    1 0 0 1
# --------------------
#   0 0 1 0    0 0 1 0 --> (34)_10 which is 105 - 71 = 34

# if there's a carry-on for 9 bits, you *DROP IT* because it must be a fixed size

## Two's complement (8-bit)
# Must fix the width and know the width

#   128 64 32 16 8 4 2 1
#  -128 64 32 16 8 4 2 1 --> Now, top power is negative

# TOP BIT (MOST SIGNIFICANT BIT< MSB) IS A SIGN BIT --> you can tell the sign by looking at the first bit
# TOGGLE AND INCREASE --> negate a binary number

# e.g., 0 1 0 0  0 1 1 1
#    toggle (replace every 0 with 1 and 1 with 0) 
#       1 0 1 1  1 0 0 0
#   increase (add one to the number)
#       1 0 1 1  1 0 0 1 

# Compute x - y as x + (-y)

## Overflow

# Once you fix the width and won't use more bits than what you start, your result will be constrained

# With k bits, you can only represent 2**k things (e.g., 8 bits --> 256 things)
#### Unsigned binary 0 .. 255
#### Signed: -128 .. 127
#   1
#   0 1 1 1  1 1 1 1 --> (127)_10
# + 0 1 0 0  0 0 0 0 --> (64)_10
# ------------------
#   1 0 1 1  1 1 1 1 --> suggest you get a negative number when you add 127 + 67 --> OVERFLOW
# If you add two numbers, the answer MUST be positive or the *TOP BIT IS 0*
# If you have two ones in the top bit

# 1   1 1 1      1 
#   1 0 1 1  1 0 0 1 --> (-71)
# x 1 0 1 1  1 0 0 1 --> (-71)
# + ----------------
#   0 1 1 1  0 0 1 0 --> OVERFLOW because it's a positive number (adding two negatives = greater negative not positive number)

# Once you deal with negative numbers, you have a fixed amount of space, therefore, you have a constained results
# If you get something that doesn't make sense, you have *OVERFLOW* or spilled over

# You have to *assume* that you're using signed bits/binary values; you don't know

# sum 2^i (i = 0...6) = 2^i - 1 = 2^7 - 1 = 127 = MOST POSTIVE VALUE in 8 bits
# -1 = (1111, 1111)_2 = -128 + (128 - 1) = -127

#-42:

# 1. Figure out 42 in binary
# 2. Pad it to 8 bits for signed
# 3. Figure out -128 + x = -42 --> x = 86

# 0 0 1 0  1 0 1 0 --> (42)_110
# 1 1 0 1  0 1 1 0 --> -128 + 86 = -42

# absolute value of 42 --> do integer division

# 42 | 0
# 21 | 1
# 10 | 0
# 5  | 1
# 2  | 0
# 1  | 1

# 42 = (0010, 1010)_2

## complement the binary pattern:

#  0 0 1 0  1 0 1 0
# toggle:
#  1 1 0 1  0 1 0 0

# increase by 1:
#  1 1 0 1  0 1 0 1

# Something that is even has 0 remainder; something that is odd has 1 remainder
