####################################################################################
# Name: Siddharth Bhatia
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
####################################################################################
# Lab 6: Recursion 2
# Demonstrate recursion as an algorithm design technique for the problem of 
# computing the (length of the) longest common subsequence of two given strings
#
# Note: Using anything other than recursion will result in a penalty
#####################################################################################

##############################################################################
# Example: The longest common subsequence of "helllowo_rld" and "!helloabcworld!"
# is "helloworld", and it has a length of 10.
#
# Therefore LLCS("helllowo_rld", "!helloabcworld!") returns 10, and
# LCS("helllowo_rld", "!helloabcworld!") returns "helloworld"
##############################################################################

def LLCS(S1, S2):
    '''
    Return the length of the longest common subsequence (LLCS) of strings S1 and S2
    '''
    # Use-It = element in question is being factored into your total result
    # Lose-It = simply recursing on the rest of list without considering the element

    # if string is empty, stop
    if len(S1) == 0 or len(S2) == 0:
        return 0

    # if the last elements of the strings are equal
    if S1[-1] == S2[-1]:
        return LLCS(S1[:-1], S2[:-1]) + 1

    lcs1 = LLCS(S1[:-1], S2)
    lcs2 = LLCS(S1, S2[:-1])

    if lcs1 > lcs2:
        return lcs1
    else:
        return lcs2

# print(LLCS("helllowo_rld", "!helloabcworld!"))

##############################################################################
# Instead of returning the length of the longest common substring, this task
# asks you to return the string itself.
##############################################################################
# Tip: You may find it helpful to copy your solution to LLCS and edit it
# to solve this problem
##############################################################################

def LCS(S1, S2):
    '''return the longest common subsequence (LCS) between strings S1 and S2'''
    # Use-It = element in question is being factored into your total result
    # Lose-It = simply recursing on the rest of list without considering the element

    # if string is empty, stop
    if len(S1) == 0 or len(S2) == 0:
        return ''

    # if the last elements of the strings are equal
    if S1[-1] == S2[-1]:
        return LCS(S1[:-1], S2[:-1]) + S1[-1]

    lcs1 = LCS(S1[:-1], S2)
    lcs2 = LCS(S1, S2[:-1])

    if len(lcs1) > len(lcs2):
        return lcs1
    else:
        return lcs2

# print(LCS("helllowo_rld", "!helloabcworld!"))
