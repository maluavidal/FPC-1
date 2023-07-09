def comb_recursive(n, k):
    if k == 0 or k == n: # caso base
        return 1
    else:
        return comb_recursive(n - 1, k - 1) + comb_recursive(n - 1, k)

def comb_iterative(n, k):
    numerator = 1
    denominator = 1

    for i in range(1, min(k, n - k) + 1):
        numerator *= n
        denominator *= i
        n -= 1

    return numerator // denominator

print(comb_iterative(4, 3))
print(comb_recursive(4, 3))
