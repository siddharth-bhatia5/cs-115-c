# Stevens Institute of Technology, 2021

##########################################
# Name: Sid Bhatia
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
##########################################
from math import floor    # E.g., floor(5.3) -> 5, floor(3.9) -> 3

######################################################################
# Task 1: Given an 8-digit decimal number representing the date,
#         calculate the day of the week using Zeller's congruence:
#
#           https://en.wikipedia.org/wiki/Zeller%27s_congruence
#
# Input:  8-digit decimal number in the format of YYYYMMDD
#
# Output: Weekday as a [0-6] number, where 
#         0: Saturday, 1: Sunday, 2: Monday, ..., 6: Friday  
######################################################################
def getWeekday(date):
    year = date // 10000 # YYYYMMDD --> YYYY
    m = date // 100 % 100 # YYYMMDD --> MM

    month_shift = 3 - m # sets January and Feburary to months 13 and 14 of previous year
    if month_shift > 0:
        m = 15 - month_shift
        year = year - 1

    q = date % 10000 % 100 # YYYYMMDD --> DD
    K = year % 100
    J = year // 100
    # weekday function based on Zeller's congruence
    weekday = (q + (13 * (m + 1) // 5) + K + K // 4 + J // 4 - 2 * J) % 7
    return weekday

# test cases
# print(getWeekday(19960229))
# print(getWeekday(20000101))
# print(getWeekday(20000102))

######################################################################
# Task 2: Create two functions, an encoder and a decoder for the
#         Caesar cipher:
#
#           https://en.wikipedia.org/wiki/Caesar_cipher
#
# Note: You can try out this cipher at the link below:
#
#           https://cryptii.com/pipes/caesar-cipher
######################################################################

######################################################################
# This provided helper function may be useful
# Input:  List of ASCII values (Ex: [72, 69, 76, 76, 79])
# Output: String (Ex. 'HELLO')       'H   E   L   L   O'
######################################################################
def asciiToString(asciiList):
    return ''.join(map(chr, asciiList))

######################################################################
# Caesar Encoder
#
# Input: A string (assume all-caps: leave everything else as-is),
#        and a shift value       (Ex. 'HELLO WORLD', 3)
#
# Output: An encoded string      (Ex. 'KHOOR ZRUOG')
#
# Hint: The ord() function converts single-character strings to ASCII
#       (Its inverse, the chr() function, is used in the provided helper)
######################################################################

def caesarEncoder(str, shift):
    # Helper Functions
    def retrieveNum(char):
        return ord(char) # returns ASCII value of character
    def encodeNum(num): # shifts the ASCII value
        if num == 32:
            return num
        elif (num + shift <= 90):
            return num + shift
        else:
            return num + shift - 24
        
    charList = list(str) # creates list of string characters
    asciiList = list(map(retrieveNum, list(str))) # creates list of ASCII values
    shift = shift % 26 # alters shift

    shiftedList = list(map(encodeNum, asciiList)) # shifts the ASCII values of list
    newList = asciiToString(shiftedList) # new encoded list

    return newList

# test cases
# print(caesarEncoder('ABCDEFGHIJKLMNOPQRSTUVWXY', 1))
# print(caesarEncoder('TESTING', 4))
# print(caesarEncoder('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 1))
# print(caesarEncoder('MORETESTING', 26))
        
######################################################################
# Decoder
# Input: A string value with all capital letters (leave everything
#        else as-is) and a shift value (Ex. KHOOR ZRUOG, 3)
# Output: A decoded string             (Ex. HELLO WORLD)
# Hint: The chr() function converts ASCII to a single-character string
######################################################################
def caesarDecoder(str, shift):
    # Helper Functions
    def retrieveNum(char):
        return ord(char) # returns ASCII value of character
    def decodeNum(num): # shifts the ASCII value
        if num == 32:
            return num
        elif (num - shift >= 65):
            return num - shift
        else:
            return num - shift + 26
    charList = list(str) # creates list of string characters
    asciiList = list(map(retrieveNum, list(str))) # creates list of ASCII values
    shift = shift % 26 # alters shift

    shiftedList = list(map(decodeNum, asciiList)) # shifts the ASCII values of list
    newList = asciiToString(shiftedList) # new decoded list

    return newList
    
# test cases
# print()
# print(caesarDecoder('BCDEFGHIJKLMNOPQRSTUVWXYZ', 1))
# print(caesarDecoder('XIWXMRK', 4))
# print(caesarDecoder('ZABCDEFGHIJKLMNOPQRSTUVWXY', 25))
# print(caesarDecoder('MORETESTING', 26))
