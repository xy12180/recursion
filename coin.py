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

print(combos_r([1], 0))
print(combos_r([2], 3))
print(combos_r([2], 1))
print(combos_r([5,2,1], 11))
print(combos_r([5,2], 11))
print(combos_r([5,3,1], 8))
print(combos_r([5,3,1], 7))
print(combos_r([5,3,1], 6))
