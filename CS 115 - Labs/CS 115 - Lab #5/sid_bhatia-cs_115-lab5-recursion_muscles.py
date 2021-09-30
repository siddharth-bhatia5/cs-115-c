# Sid Bhatia
# CS 115-C
# Lab #5 - Recursion Muscles
# I pledge my honor that I have abided by the Stevens Honor System.

"""
In this lab, you will write a few Python functions using recursion. You must only
use recursion, conditional statements (if, else, elif), list or string indexing
and slicing. Some of these problems can be written without using recursion, e.g.
using map, filter, reduce, filter or other looping structures. However, the
objective here is to build your recursion muscles, so only stick to recursion. There
will be a deduction for using any loops.

Do not use built-in functions (e.g. len, sum, etc.). However, your functions may
call other functions that you write yourself.

Please be sure to name your functions exactly as specified for grading
purposes.
"""

def dotProduct(L, K):
    """
    Outputs the dot product of lists L and K.
    Assume that the lists are equal in length.
    If two lists are empty, output should be 0.0.
    """

    if L == [] or K == []:
        return 0.0
    return L[0] * K[0] + dotProduct(L[1:], K[1:])

# print(dotProduct([5,3], [6,4]))

def removeAll(e, L):
    """
    Takes in an element e and a list L. Then, removeAll should
    return another list that is identical to L except that all elements identical to e have
    been removed.
    """

    if(L == []):
        return []
    elif(L[0] != e):
        return [L[0]] + removeAll(e, L[1:])
    else:
        return removeAll(e, L[1:])
    

# L[:-1] gets all the elements up to the last index
# L[-1:] gets the last element of the list but in the form of a list
# L[-1:] = [L[-1]]

# print(removeAll(42, [55, 77, 42, 11, 42, 88]))

def geometricSeq(n, f, b):
    """
    Takes in elements n, f, and b, where n is the nth number
    in the sequence, f is the multiplicative factor, and b is base case for when n=1.
    """
    if (n == 1):
        return b
    else:
        return (f * geometricSeq(n - 1, f, b))  

# print(geometricSeq(1, 2, 5))
# print(geometricSeq(3, 3, 1))
# print(geometricSeq(3, 2, 10))

def deepReverse(L):
    if(L == []):
        return []
    elif(isinstance(L[-1], list)): # isinstance() checks whether an object is an object
        return ([deepReverse(L[-1])] + deepReverse(L[:-1]))
    else:
        return([L[-1]] + deepReverse(L[:-1]))

# print(deepReverse([1, 2, 3]))
# print(deepReverse([1, [2, 3], 4]))
# print(deepReverse([1, [2, [3, 4], [5, [6, 7], 8]]]))
