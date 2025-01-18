# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Input: coins = [2], amount = 3
# Output: None

# Input: coins = [1], amount = 0
# Output: 0

def combos_r(coins, a):
    
    if a == 0:
        return 0

    cs = pick(coins, a)
    if not cs:
        return None

    try:
        for c in cs:
            return 1 + combos_r(coins, a-c)
    except TypeError:
        return None

def pick(coins, a):
    return [c for c in coins if c <= a]

def combos(coins, a):
    coins = sorted(coins, reverse=True)
    return combos_r(coins, a)

def test():
    print("testing...")
    assert combos([1], 0) == 0
    assert combos([2], 3) == None
    assert combos([2], 1) == None
    assert combos([1,2,5], 11) == 3
    assert combos([5,2], 11) == None
    assert combos([1,3,5], 8) == 2
    assert combos([1,3,5], 7) == 3
    assert combos([1,3,5], 6) == 2

test()
print("passed")
