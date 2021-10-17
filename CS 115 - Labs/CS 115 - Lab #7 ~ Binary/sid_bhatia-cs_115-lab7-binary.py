####################################################################################
# Name: Sid Bhatia
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
####################################################################################


# The binary format you'll be working with for this assignment is called R2L,
# as it is a right-to-left representation.
####################################################################################
## Ex: 8 in decimal is 1000 in standard binary (2^3),
## and represented as a list [0, 0, 0, 1] in our R2L representation.
####################################################################################

# Notice that this makes it very easy to work with binary,
# by using num[0] to grab the least significant bit (2^0)!
#
# Please fill out the following 4 functions below using recursion, as specified.

# Given an integer x >= 0, convert it to the R2L binary format.
# Take note that both [] and [0] are used to represent 0 in R2L
def decimalToBinary(x):
    if x == 0:
        return []
    else:
        return [x % 2] + decimalToBinary(x // 2)

# test case
# print(decimalToBinary(10))

# 10

# 10 | 0
# 5 | 1
# 2 | 0
# 1 | 1

# Given an R2L formatted number, return the integer it is equivalent to.
# The function should function with both [] and [0] returning 0.
def binaryToDecimal(num):
    if len(num) == 0:
        return 0
    elif num[-1] == 1:
        return 2**(len(num) - 1) + binaryToDecimal(num[:-1])
    else:
        return binaryToDecimal(num[:-1])

# test case
# print(binaryToDecimal([0,0,0,1]))

# Given an R2L formatted number, return an R2L equivalent to num + 1
# If you need to increase the length, do so. Again, watch out for 0
def incrementBinary(num):
    if not num or num == [0]:
        return [1]
    if num[0] + 1 == 1:
        return [1] + num[1:]
    else:
        return [0] + incrementBinary(num[1:])

# test cases
# print(incrementBinary([0,0,0,1]))
# print(incrementBinary([0,0,0,1,1]))
# print(incrementBinary([1,1,1,1,1]))

# Given 2 R2L numbers, return their sum.
## You MUST implement recursively the algorithm for bit-by-bit addition as taught in class,
## you may NOT do something like decimalToBinary( binaryToDecimal(num1) + binaryToDecimal(num2) ).
# Make sure to figure out what to do when num1 and num2 aren't of the same length!
# (and be sure you can add [] and [0])
## Tip: Try this on paper before typing it up
def addBinary(num1, num2):

    def carryNum(num1, num2, carry):
        if not num1:
            if carry == 1:
                return incrementBinary(num2)
            else:
                return num2
        if not num2:
            if carry == 1:
                return incrementBinary(num1)
            else:
                return num1
        if num1[0] + num2[0] + carry == 0: # 0 0 w/0 carry
            return [0]+ carryNum(num1[1:],num2[1:],0)
        if num1[0] + num2[0] + carry == 1:
            return [1] + carryNum(num1[1:],num2[1:],0)
        if num1[0] + num2[0] + carry ==2:
            return [0] + carryNum(num1[1:],num2[1:],1)
        if num1[0] + num2[0] + carry ==2:
            return [1] + carryNum(num1[1:],num2[1:],1)
    return carryNum(num1, num2, 0)

#    1 1 1 1 1 0 0
#            0 0 1
#   + ------------
#    1 1 1 1 1 1 0 1

#    1  1 1
#    1 1 1 1 1
#  + 1 1 1 1 0
# ------------
#   1 1 1 1 0 1
