def fibonacci_period_mod_k(k):
    period = 0
    f0, f1 = 0, 1 % k

    while True:
        period += 1
        f0, f1 = f1, (f0 + f1) % k

        if (f0, f1) == (0, 1 % k):
            break

    return period


print(f"period = {fibonacci_period_mod_k(3)}")
