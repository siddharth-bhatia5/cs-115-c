# Sid Bhatia
# CS 115-C
# Lecture #9 - Advanced Map

# Sample Problem: Compute average value in the list
# Given a list
# Demonstrate multiple argument map
# {4, 1, 3, 5, 7, 8, 6, 9]
# [4, 2, 3, 5, 6, 7, 7, 9]

def avg_of_three(x1, x2, x3):
    """
    Function that computes the average of three numbers;
    the function that map uses on the list.
    """
    return (x1 + x2 + x3) // 3

# map f(f,l)
# go through l and apply f to each item ONE by one

# map(f, l1, l2, l3, l4, l5, ...)

# process described by f should be able to
# treat as many items at a time as there are list

# map(avg_of_three, l1, l2, l3)

# imagine you have three lists with values lining up (1, 4, 5) and (5,1,9)

#   [4, 1, 5, 9]        <-- l1 --> [1,5]
#       [4, 1, 5, 9]    <-- l2 --> [4, 1]
# {4, 1, 5, 9]          <-- l3 --> [5, 9]
#                                  [3, 5]

#   [4, 1, 5, 6, 7, 1, 7, 8, 9]
#       [4, 1, 5, 6, 7, 1, 7, 8, 9]
# [4, 1, 5, 6, 7, 1, 7, 8, 9]

# when you have the negative index, you just have the length of the list - 1

# l1 = l[1:-1] = l[1:len(l)-1]
# l2 = l[:-2] = l[0:len(l)-2]
# l3 = l[2:] = l[2:len(l)]



