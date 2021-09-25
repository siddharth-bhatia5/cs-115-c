# Sid Bhatia
# CS 115-C
# Lecture 10 - Multi-List Map Function

# more practice with multi-list map function

# functools.reduce

# new syntax: lambda expressions

# list of squares

 

from math import sqrt, ceil

list(range(ceil(sqrt(100))))

 

list(range(ceil(sqrt(99))))

 

list(range(ceil(sqrt(101))))

 

def list_of_squares(bound):

    ints = range(ceil(sqrt(bound)))

    def square(x):

        return x**2

    result = map(square, ints)

    return (list(result))

 

# multi-list map

 

list1 = [5,4,6]

list2 = [2,6,1]

 

# list1 + list2 = [5,4,6,2,6,1]

def list_sum(l1, l2):

    def add(x, y):

        return x+y

 

   

    result = map(add, l1, l2)

    return (list(result)

 

    return map(def f(x1,x2): return x1 + x2, l1, l2)

    return list(result)

 

# Keyboard Interrupt

a = 4 + 5

def h(x):

    return x ** x

 

h = lambda x: x**2

add = lambda x1, x2: x1+x2

 

def list_of_sqaures(bound):

    ints = range(ceil(sqrt(bound)))

    result = map(lambda x: x**2, ints)

    return list(result)

 

def list_sum(l1, l2):

    result = map(lambda x1, x2 : x1 + x2, l1, l2)

    return list(result)

 

from functools import reduce

 

def sum_via_reduce(L):

    def add(x1, x2):

        return x1+x2

    return reduce(add, L)

 

sum_via_reduce(range(10))
