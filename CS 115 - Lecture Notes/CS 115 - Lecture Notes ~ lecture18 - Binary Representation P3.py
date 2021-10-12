# Sid Bhatia
# CS 115-C
# Lecture #18 - Binary Representation P3


# ***MIDTERM EXAM:***
# Python Basics
# Map and Reduce; Lambda Expression; Filter
# Recursion w/Use-It or Lose-it (most likely) but also check head-or-tail
# Binary question --> conversion, addition, and multiplication could be on exam
# Negative numbers won't be on it

# Closed book and closed notes but have 1 study sheet
# It'll have the pledge --> PDF

# ----------------------------------------------------

# Converting Between Bases

# 1101_2 --> Base 10
# 1 = included; 0 = not included

# 1101_2 --> 8 + 4 + 0 + 1 = 13

# 25_10 --> Base 2
# Half it multiple times and drop fractional part

# Base 2 Multiplication

#  111 x 101

#       1 1 1
#     x 1 0 1
#     -------
#   (1)(1)1 1 1
#   0 0 0
#   1 1 1
#   ---------
#  1 0 0 0 1 1 = 32 + 2 + 1 = 35
#   even sum = 0; odd sum = 1


# Multiplication w/Russian Peasants:
# Keep halving (integer dividing) the first number and doubling the second number; add the #s that correspond to the 'odd' first number term

# 21 x 6:

# 21 6 --> selected
# 10 12
# 5  24 --> selected
# 2  48
# 1  96 --> selected

# therefore, 21 x 6 = 6 + 24 + 96 = 126

# 33 x 7

# 33 7 --> selected
# 16 14
# 8  28
# 4  56
# 2  112
# 1  224 --> selected

# therefore, 33 x 7 = 7 + 224 = 231

#           111
#    x   100001
#    ----------
#           111
#          000
#         000
#        000
#       000
#      111
#   -----------
#      11100111

# Binary subtraction wouldn't be on the exam

# Negative Numbers:
# Sign and magnitude: 1 .. 1
# Biased binary (BCD)

# One's Complement (-3): 1 .. 00
# First bit is the sign; 1 = negative sign

# 0000, 0011

#   1111, 1100
#   0000, 0001
# + ----------
#   1111, 1101

# (1)011
# + 101
# -----
#  000 --> any 'care over' greater than the number of bits are thrown aways

# Two's Complemen: one's complement then increase
