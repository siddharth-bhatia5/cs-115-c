##########################################
# Name: Sid Bhatia
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
##########################################

# Import reduce from the functools package
from functools import reduce

#######################################################################################
# Task 1: Use reduce to determine if all elements in a boolean list are true
def all_true(lst):
    def check_boolean(value1, value2):
        if (value1 == False) or (value2 == False):
            return False
        return True
    return reduce(check_boolean, lst)

# lst1 = [False, False, True]
# lst2 = [True, True, False]
# lst3 = [True, True, True]
# lst4 = [True, True, True, True]
# print(all_true(lst1))
# print(all_true(lst2))
# print(all_true(lst3))
# print(all_true(lst4))
# print()

#######################################################################################
# Task 1.1: Use reduce to determine if AT LEAST one element in a boolean list is true
# Hint: Should be very similar to the above function
def one_true(lst):
    def check_boolean2(value1, value2):
        if (value1 == True) or (value2 == True): # checks if one of the elements are true
            return True
        return False # otherwise, returns false
    return reduce(check_boolean2, lst)

# print(one_true(lst1))
# print(one_true(lst2))
# print(one_true(lst3))
# print(one_true(lst4))

# lst5 = [False, False, False]
# print(one_true(lst5))

#######################################################################################
# Task 2: Use map and reduce to return how many elements are True in a boolean list
def count_true(lst):
    def find_true(value): # converts boolean list into list of integers
        if value == True:
            return 1
        return 0

    def count_true(value1, value2):
        return value1 + value2 
    return reduce(count_true, list(map(find_true, lst))) # summates number of Trues
                  
# print(count_true(lst1))
# print(count_true(lst2))
# print(count_true(lst3))
# print(count_true(lst4))

# use map to create a list of just numbers from the boolean list
# then, use reduce to count the number of True values to count the number of elements

# reduce on the outside, map on the inside
        

# This function is provided for you
# Gets a list of strings through the command line
# Input is accepted line-by-line
def getInput():
    lst = []
    txt = input()

    while(len(txt) != 0):
        lst.append(txt)
        txt = input()

    return lst

# Task 3: Get the longest string in the list using map and reduce, and print it out
# 'strings' is a list of input strings e.g. [ 'hello', 'world' ]
# Hint: The 'map' part of your program should take a string s into a length-2 list [len(s), s].
def getLongestString():
    strings = getInput()

    def create_sub_list(s):
        """Creates sub lists with the length of the string and the string itself"""
        return [len(s), s] 

    def compare(lst1, lst2):
        """Compares the length of the string by checking the first element of the sub lists"""
        if lst1[0] > lst2[0]:
            return lst1
        else:
            return lst2

    # returns the list with the greatest string
    return reduce(compare, list(map(create_sub_list, strings)))[1] # accesses the string by indexing the second element

    # reduce[compare, lst] gives you the index of the list with two elements including the longest string
    # therefore, return reduce[compare, lst][1] will give you the answer

# print(getLongestString())
