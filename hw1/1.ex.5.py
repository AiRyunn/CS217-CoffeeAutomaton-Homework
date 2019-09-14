def combination_dp_mod_2(n, k):
    if k < 0 or k > n:
        return 0
    elif n == 0:
        return 1

    """
    C = [0] * (k + 1)
    for i in range(n + 1):
        C[0] = 1
        for j in range(min(i, k), 0, -1):
            C[j] = (C[j] + C[j - 1]) % 2
    return C[k]
    """
    C = [None] * (n + 1)
    for i in range(n + 1):
        C[i] = [0] * (k + 1)
        C[i][0] = 1
        for j in range(1, min(i + 1, k + 1)):
            C[i][j] = (C[i - 1][j] + C[i - 1][j - 1]) % 2
    return C[n][k]


print(combination_dp_mod_2(5, 3))
