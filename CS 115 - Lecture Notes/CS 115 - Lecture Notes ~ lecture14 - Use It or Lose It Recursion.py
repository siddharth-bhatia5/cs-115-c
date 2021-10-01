# Sid Bhatia
# CS 115-C
# Lecture 14 - Use It or Lose It Recursion

# Break down non-empty list as first/rest (head/tail)
# Base case will be the empty list: []

L = [[5, 10, 20], 3, 'b']

def recursive_list_function(L):
    if L == []: # alternatively, if not L:
        result = base_val
    else:
        head, tail = L[0], L[1:]
        result = recursive_step(head, tail)
    return result

def recursive_length(L):
    base_val = 0
    def recursive_step(h, t):
        head_contribution = 1
        tail_contribution = recursive_length(t)
        return head_contribution + tail_contribution
    if not L:
        result = base_val
    else:
        head, tail = L[0], L[1:]
        result = recursive_step(head, tail)
    return result

print(recursive_length(L))
print(recursive_length([]))

def recursive_deep_length(L):
    """
    Returns the "deep length" or actual length of list(s).
    """
    base_val = 0
    def recursive_step(h, t):
        if isinstance(h, list):
            head_contribution = recursive_deep_length(h)
        else:
            head_contribution = 1
            
        tail_contribution = recursive_deep_length(t)
        return head_contribution + tail_contribution
    if not L:
        result = base_val
    else:
        head, tail = L[0], L[1:]
        result = recursive_step(head, tail)
    return result

print(recursive_deep_length(L))
LL = [[], [[[], [], []]]]
print(recursive_deep_length(LL))

def recursive_map(f, L):
    base_val = [] # what if recursive_map(f, [])?
    def recursive_step(h, t):
        head_contribution = f(h)
        tail_contribution = recursive_map(f, t)
        overall = [head_contribution] + tail_contribution
        return overall
    if not L:
        result = base_val
    else:
        head, tail = L[0], L[1:]
        result = recursive_step(head, tail)
    return result

print(recursive_map(lambda x: x*2, list(range(0, 20))))

# branch recursion
# aka Use-It-or-Lose-It
# count combinations
# choose
# choose(n, k): count the number of ways that k distinct items might be chosen from a group of n

# (a + b)**n = \sum_{i = 1..k} choose(n,k) a**(n-k) * b**k

def choose_rec(n, k):
    """
    Count the number of ways that k distinct items might be chosen from a group of n

    Assume 0 <= k <= n
    """
    # NB: You can choose 0 things out of n in exactly 1 way
    # NB: You can choose n things out of n in exactly 1 way

    if k == 0 or k == n:
        result = 1
    else:
        # 0 < k < n
        # focus on the first of the n items
        # two options:
        ## use first: then your left with k-1 things to pick, out of n-1
        ## lose first: then need to pick k out of n-1
        use_it = choose_rec(n-1, k-1)
        lose_it = choose_rec(n-1, k)
        result = use_it + lose_it
    return result

print(choose_rec(3, 0))
print(choose_rec(4, 4))
print(choose_rec(6, 4))
