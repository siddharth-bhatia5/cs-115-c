# Sid Bhatia
# CS-115
# Lecture #11 -

from functools import reduce
import math

l = [30, 12, 43, 20, 14, 23]

print(max(l))

print(reduce(max, l)) # prints max value of the list

def my_max(x,y):
    result = 0
    """
    Function that returns that max of two values.
    """
    if (x > y):
        reduce = x
    else:
        reduce = y

    return reduce # only one return statement for good practice

print(my_max(10, 30))

print()
print(reduce(my_max, l))

def my_max2(x,y): # statements don't get anything done
    result = x if x > y else y # know as if-else expression
    # expressions has values
    return result

def my_max3(x,y):
    # essentially a lambda function
    return x if x > y else y

print(reduce(my_max3, l))

print()
# lambda function defines a function without parentheses and return statement
max_value = reduce(lambda x,y: x if x > y else y, l)

print(max_value)

min_value = reduce(lambda x,y: x if x < y else y, l)
print(min_value)

sum_value = reduce(lambda x,y: x+y, l)
average = "\nThe average is: " + str(sum_value // len(l))
print(average)

print()
product_value = reduce(lambda x,y: x*y, l)
power = 1 / len(l)

# geometric mean = Pi of list with the root of the number of items in list
geometric_mean = math.pow(product_value, power)

print(geometric_mean)

def is_even(x):
    if x % 2 == 0:
        return True
    return False

print(is_even(10))
print(is_even(1))

def evens(bound):
    ints = range(bound+1)
    result = filter(is_even, ints) # filter can create a list of less values
    return list(result)

# filter(predicate, list)

print(evens(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 2, 4, 6, 8]


def three_multiples(bound):
    ints = range(bound)
    result = list(filter(lambda x: True if x % 3 == 0 else False, ints))
    return result

print(three_multiples(10))
