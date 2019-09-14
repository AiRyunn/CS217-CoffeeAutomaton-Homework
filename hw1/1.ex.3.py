def combination_rec(n, k):
    if k < 0 or k > n:
        return 0
    elif n == 0:
        return 1

    return combination_rec(n - 1, k) + combination_rec(n - 1, k - 1)


print(combination_rec(5, 3))
