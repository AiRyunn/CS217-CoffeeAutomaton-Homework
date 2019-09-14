def euclid(a, b):
    while b > 0:
        r = a % b # so a = bu + r
        if r == 0:
            return b
        s = b % r # so b = rv + s
        a = r
        b = s
    return a
