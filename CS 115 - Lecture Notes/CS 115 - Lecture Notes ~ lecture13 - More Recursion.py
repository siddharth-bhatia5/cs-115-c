# Sid Bhatia
# CS 115-C
# Lecture #13 - More Recursion

# Factorial
# n! = 1 * 2 * 3 * 4 ... * n

# n! = 1 * 2 * 3 ... * (n-1) * n
# n! = (n-1)! * n
# 0! = 1
# 1! = 1

from math import factorial

print(factorial(10))

def rec_factorial(n):
    """
    Computes the factorial recursively.
    """
    if n == 0: # base case: 0! = 1
        return 1
    return n * rec_factorial(n-1)

print(rec_factorial(10))

def rec2_factorial(n):
    """
    Computes the factorial recursively using 'result.'
    """
    if n == 0: # base case: 0! = 1
        result = 1
    elif n == 1:
        result = 1
    else:
        prev_result = rec2_factorial(n-1)
        result = prev_result * n
    return result

print(rec2_factorial(10))

# if-expression: <value-when-true> if <condition> else <value-when-false>

def rec3_factorial(n): # back-slash = ignore new line
    return 1 if n == 0 else \
           1 if n == 1 else \
           rec3_factorial(n-1) * n

print(rec3_factorial(1000))

def rec4_factorial(n):
    return 1 if n == 0 or n == 1 else \
           rec4_factorial(n-1) * n

print(rec4_factorial(5))

def get_nth_even(n):
    """
    Return the nth even number where first (n = 1) is 0."""
    if n == 1: # base case
        result = 0
    else:
        prev_result = get_nth_even(n-1)
        result = prev_result + 2
    return result

print(get_nth_even(5))

def get_nth_odd(n):
    """
    Return the nth odd number where first (n = 1) is 1."""
    if n == 1: # base case
        result = 1
    else:
        prev_result = get_nth_even(n-1)
        result = prev_result + 2
    return result

print(get_nth_odd(10))

# recursion using two functions calling each other
# known as mutual recursion

def even_odd(n):
    if n == 1:
        result = 1
    else:
        prev_result = odd_even(n-1)
        result = prev_result + 2

def odd_even(n):
    if n == 1:
        result = 0
    else:
        prev_result = even_odd(n-1)
        result = prev_result = 2
    return result

print(even_odd(3))
print(odd_even(3))

def my_len(l):
    if l == []:
        result = 0
    else:
        prev_result = my_len(l[1:])
        result = prev_result + 1
    return result

print(my_len([1,2,3]))
