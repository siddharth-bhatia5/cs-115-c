# Sid Bhatia
# CS 115-C
# Lab #5 - Notes ~ Recursion Muscles

# When using recursion, you usually call the first value or the first character

# Find all subsets of the string 'dog': e.g., 'do', 'og', 'd, 'o', 'dg', 'g'

# Have to do use it or lose it

# def substring(s):
    # if len(s) == 0:
    #   return ''
    # return list(s(0) + substring(s(1:))) + list(substring(s(1:))

def substring(s):
    if len(s) == 0:
        return ''
    return list(s[0] + substring[1:]) 
