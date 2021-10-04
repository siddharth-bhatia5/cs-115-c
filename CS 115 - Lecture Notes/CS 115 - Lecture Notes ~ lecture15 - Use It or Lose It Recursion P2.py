# Sid Bhatia
# CS 115-C
# lecture15 - Use It or Lose It Recursion P2

# More Use It Or Lose It
# Counting combinations
# A set of n items and want to pick <= n out of them
# How many different ways can we do that
# [1, 2, 3, 4]
# [[1, 2,], [1, 3], [1, 4], [2,3], [2,4], [3,4]]

def choose(n,k):
    """
    Count the k-combinations from a universe of size n.
    """
    # Base case:
    ## If we are picking no items (k is zero)
    ### Then, there is exactly one way ([])
    ## If we are packing all the items (k == n),
    ### Then, there is exactly one way
    if k == 0 or k == n:
        result = 1
    else:
        # use it or lose it
        # focus on, say, the first item

        # how many k-combinations are there that include the first item
        use_it = choose(n-1, k-1)
        lose_it = choose(n-1, k)
        result = use_it + lose_it
    return result

print(choose(4,2))

# Powerset
# [1, 2, 3] --> [ [], [1], [2], [3], [1,2], [1,3], [2,3], [1, 2, 3]]
# The size of the powerset is 2 ** n
#   1   2   3   4   ...  (n-1)   n
#   Y   Y   N   N   ... Y        N      [1, 2, ..., (n-1)]
# 2 ** 3 = 1 + 3 + 3 + 1
# (a+b)**n = \sum_{k=0..n} \choose(n,k) a**(n-k) b ** k
# 2**n = \sum choose(n, k)

def power_set(S):
    if not S:
        result = [[]]
    else:
        first, rest = S[0], S[1:]
        # use-it or # lose-it
        lose_it = power_set(rest)

        # use-it should enumerate all the subsets that do include the first
        def prepend_first(L):
            return [first] + L
        use_it = list(map(prepend_first, lose_it))
        result = use_it + lose_it
    return result

print(power_set([1,2]))

def combinations(S, k):
    return list(filter(lambda L: len(L) == k, power_set(S)))

print(combinations(list(range(1,11)), 2))

def combination_rec(S, k):
    if k == 0:
        result = [[]]
    elif not S:
        # here k > 0 = len(S)
        result = 0
    else:
        first, rest = S[0], S[1:]
        lose_it = combinations(rest, k)
        use_it_helper = combinations(rest, k-1)
        def prepend_first(L):
            return [first] + L
        use_it = list(map(prepend_first, use_it_helper))
        result = use_it + lose_it
    return result

print(combination_rec([1,2,3], 1))
print(combination_rec([1,2,3], 2))
