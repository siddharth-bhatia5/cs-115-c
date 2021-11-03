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
# Input:  8-digit decimal number in the format of YYYYMMDD --> 20210923
#
# Output: Weekday as a [0-6] number, where 
#         0: Saturday, 1: Sunday, 2: Monday, ..., 6: Friday  
######################################################################
def getWeekday(date):

    year = date // 10000 # YYYYMMDD --> YYYY
    m = date // 100 % 100 # YYYYMMDD --> MM
    q = date % 10000 % 100 # day of the month
    
    K = year % 100 # year of the century (year % 100)
    J = year // 100 # zero-based century

    weekday_congruence = (q + (13 * (m + 1) // 5) + K + (K // 4) + (J // 4) - 2 * J) % 7
    
    return weekday_congruence

print(getWeekday(20211221))

######################################################################
# Task 2: Create two functions, an encoder and a decoder for the
#         Caesar cipher:
#
#           https://en.wikipedia.org/wiki/Caesar_cipher
#
# Note: You can try out this cipher at the link below:
#
#           
######################################################################

######################################################################
# This provided helper function may be useful
# Input:  List of ASCII values (Ex: [72, 69, 76, 76, 79])
# Output: String (Ex. 'HELLO')       'H   E   L   L   O'
######################################################################
def ascii_to_string(asciiList):
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
def move_string(str, shift):
        letter_list = list(str) # converts string into list of characters

        def get_value(char):
            return ord(char) # retrieves the ASCII value of the character
        list_num = list(map(get_value, letter_list)) # retrieves the list of the ASCII values

        def increase_num(num):
            return num + shift # shifts the value of number to the shift value

        shifted_num_list = list(map(increase_num, list_num))

        new_string = ascii_to_string(shifted_num_list)
        return new_string

def caesar_encoder(str, shift):
    return move_string(str, shift)

######################################################################
# Decoder
# Input: A string value with all capital letters (leave everything
#        else as-is) and a shift value (Ex. KHOOR ZRUOG, 3)
# Output: A decoded string             (Ex. HELLO WORLD)
# Hint: The chr() function converts ASCII to a single-character string
######################################################################
def caesar_decoder(str, shift):
    return move_string(str, shift * -1)

# test cases
# print(caesar_encoder("HELLO WORLD", 3))
# print(caesar_decoder("KHOOR#ZROUG", 3))
# print(caesar_encoder("abc", 3))
# print(caesar_decoder("def", 3))

# print(caesar_encoder("HELLO WORLD", 17))
# print(caesar_decoder("YV]]`1h`c]U", 17))
