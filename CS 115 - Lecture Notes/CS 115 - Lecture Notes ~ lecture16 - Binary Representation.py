# Sid Bhatia
# CS 115-C
# Lecture #16 - Binary Representation

# What is the number 4312?

# 4 * 10**3 + 3 * 10**2 + 1 * 10**1 + 2 * 10**0
# 4000 + 300 + 10 + 2 = 4312

# What is 4312 in base 20?
# 20^2      20^1        20^0
# 1          3            2
# 1 * 20^3 + 3 * 20^1 + 2 * 20^0 = 400 + 60 + 2 = 462

# Arbitrary Bases (base "b")
# What is 5 in ...
# Base 2 =(101)_2
# Base 3 =(12)_3
# Base 4 =(11)_4
# Base 5 = (10)_5
# Base 6 = (5)_6
# Base 42 = (5)_6

# In all bases, the number b in base b = (10)_b

# When the base is larger than the base b, the number is just base b

# Is there such a thing as Base 1? Known as uniary
# 1111 = 4 because you add up it up

# digits 0 and 1 referred to as "bits" that's short for binary digits

# Convert 1101_2 to base 10
# 8 + 4 + 1 = 13

# Convert 10110_2 to base 10
# 16 + 4 + 2 = 22


# Convert 25_10 to base 2
# 11001


# 25 --> Keep halving it and look at reminder; if odd, assign 1; if even, assign 0
# 25 | 1
# 12 | 0
# 6 | 0
# 3 | 1
# 1 | 1

# read bits from bottom up --> 11001

# 115 | 1 --> (115 - 1) / 2  = 57
# 57 | 1 --> (57 - 1) / 2 = 26
# 28 | 0 --> (28 - 0) / 2 = 14
# 14 | 0 --> (14 - 0) / 2 = 7
# 7 | 1 --> (7 - 1) / 2 = 3
# 3 | 1 --> (3 - 1) / 2 = 1
# 1 | 1

# Therefore, 115_10 = 1110011_2
