# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Input: coins = [2], amount = 3
# Output: -1

# Input: coins = [1], amount = 0
# Output: 0

def combos(coins, a, level=0):
    if a == 0:
        return 0

    cs = pick(coins, a)
    if not cs:
        return -1 if level==0 else None

    try:
        return min(1 + combos(coins, a-c, level+1) for c in cs)
    except TypeError:
        return -1

def pick(coins, a):
    return [c for c in coins if c <= a]

print(combos([1], 0))
print(combos([2], 3))
print(combos([2], 1))
print(combos([5,2,1], 11))
