# Sid Bhatia
# CS 115-C
# Lecture #12 - Recursion

# Focus on 'what' more than 'how'
# 'What' is more big picture
# 'How' is more detailed
# False sense of progress
# -> Easy to get something that kind of works
# Golden goal in coding is to write provably correct code

# Recursion has a more of 'all-or-nothing' feel

# To understand recursion, you must first understand recursion
# To iterate is human, to recurse is divine

# Re-curse
# Define function recursively

# Natural numbers: 1, 2, 3, ... (N)

# A natural number is either 1 or is one more than a natural number

# Why is 3 a natural number?

# B/c 2 is
# ... Why is 2 a natural number?
# ... B/c 1 is
# ... ... why is 1 a natural number?
# ... ... Just b/c

# Defining list as a recursive concept

# A list is either [] or an item pre-pended to another list

# Define a function that produces a list of n 1's

[1,1,1,1]

def ones(n):
    """
    Produce a list with n 1's.
    """
    # You could do this using 'list multiplication'
    # 'hi' + 'hi' -> 'hihi'
    # 'hi' * 2 -> 'hihi'
    result = n * [1]
    return result

print(ones(10))

print(-2 * [1,2]) # gives an empty list

def rec_ones(n):
    """
    Produce a list of n 1's.
    Note that in a list of n 1's there is a list of n-1 1's.
    """
    if n <= 0:
        result = []
    else:
        previous_result = rec_ones(n-1)
        result = [1] + previous_result
    return result

print(rec_ones(3))
print(rec_ones(20))
print(rec_ones(0)) # empty list
print(rec_ones(-2)) # empty list
    



