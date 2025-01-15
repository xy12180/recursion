"""
functions: iterative, recursive, and tail recursive
"""

def len_i(s):
    """iteration"""
    n = 0
    for _ in s:
        n += 1
    return n

def len_r(s):
    """recursion"""
    if not s:
        return 0
    else:
        first, rest = s[0], s[1:]
        return 1 + len_r(rest)

def len_tr(s):
    def len_tr_helper(s, a=0):
        """tail recursion"""
        if not s:
            return a
        else:
            first, rest = s[0], s[1:]
            return len_tr_helper(rest, a + 1)
    return len_tr_helper(s)

def test():
    print("testing...")
    s = [1, 2, 3]
    assert len_i(s) == 3
    assert len_r(s) == 3
    assert len_tr(s) == 3

    import random
    n = random.randint(10, 100)
    s = range(n)
    assert len_i(s) == n
    assert len_r(s) == n
    assert len_tr(s) == n

test()
print("passed")

