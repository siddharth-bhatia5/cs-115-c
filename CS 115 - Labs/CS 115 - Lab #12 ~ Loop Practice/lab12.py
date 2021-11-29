# Sid Bhatia
# CS115-C
# I pledge my honor that I have abided by the Stevens Honor System.
# Lab 12 - Loops Practice

import random

def shuffledNumbers(n):
    '''
    Write a function implementing the following pseudocode:

    1. Check that n is non-negative, and return an empty list otherwise
    2. Initialize a length-n list “out” so that, for all i, entry i, in “out” has value i.
    3. For i from n-1 down to 1
    4.      Pick an int j at random between 0 and i inclusive
    5.      If j is less than i, swap out[i] and out[j]
    6. Return out
    Tip: For step 4, call random.randint(0, i) and make sure to import random. 
    '''
    if n < 0:
        return []
    else:
        out = []
        for i in range(n):
            out.append(i)
        for i in range(n-1, 1, -1):
            j = random.randint(0,i)
            if j < i:
                temp = out[i]
                out[i] = out[j]
                out[j] = temp
    return out

print(shuffledNumbers(10))

def string_times(str, n):
    '''
    Given a string and a non-negative int n, return a larger string that is n copies of
    the original string.

    string_times('Hi', 2) → 'HiHi'
    string_times('Hi', 3) → 'HiHiHi'
    string_times('Hi', 1) → 'Hi' 
    '''
    return str * n

# print(string_times('Hi',2))

def front_times(str, n):
    '''
    Given a string and a non-negative int n, we'll say that the front of the string is the
    first 3 chars, or whatever is there if the string is less than length 3. Return n
    copies of the front.

    front_times('Chocolate', 2) → 'ChoCho'
    front_times('Chocolate', 3) → 'ChoChoCho'
    front_times('Abc', 3) → 'AbcAbcAbc'
    '''
    if len(str) < 3:
        return str * n
    else:
        substring = str[0:3]
        return substring * n

# print(front_times('Chocolate', 3))

def string_splosion(str):
    '''
    Given a non-empty string like "Code" return a string like "CCoCodCode".

    string_splosion('Code') → 'CCoCodCode'
    string_splosion('abc') → 'aababc'
    string_splosion('ab') → 'aab'
    '''
    result = ''
    for i in range(len(str)):
        result += str[:i+1]
    return result

# print(string_splosion('Code'))

def last2(str):
    '''
    Given a string, return the count of the number of times that a substring length 2
    appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields
    1 (we won't count the end substring).

    last2('hixxhi') → 1
    last2('xaxxaxaxx') → 1
    last2('axxxaaxx') → 2
    '''
    end_sub = str[-2:]
    count = -1
    for i in range(len(str)-1):
        sub = str[i] + str[i+1]
        if sub == end_sub:
            count += 1
    if count == -1:
        return 0
    return count

# print(last2('hixxxhi'))
# print(last2('xaxxaxaxx'))
# print(last2('axxxaaxx'))

def array_count9(nums):
    '''
    Given an array of ints, return the number of 9's in the array.

    array_count9([1, 2, 9]) → 1
    array_count9([1, 9, 9]) → 2
    array_count9([1, 9, 9, 3, 9]) → 3
    '''
    count = 0
    for i in range(len(nums)):
        if nums[i] == 9:
            count += 1
    return count

# print(array_count9([1, 9, 9, 3, 9]))

def array_front9(nums):
    '''
    Given an array of ints, return True if one of the first 4 elements in the array is a 9.
    The array length may be less than 4.

    array_front9([1, 2, 9, 3, 4]) → True
    array_front9([1, 2, 3, 4, 9]) → False
    array_front9([1, 2, 3, 4, 5]) → False 
    '''
    if len(nums) < 4:
        for i in range(nums):
            if nums[i] == 9:
                return True
        return False
    else:
        for i in range(0,4):
            if nums[i] == 9:
                return True
        return False

# print(array_front9([1, 2, 9, 3, 4]))
# print(array_front9([1, 2, 3, 4, 9]))
# print(array_front9([1, 2, 3, 4, 5]))


