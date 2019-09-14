carry = 0
for i in range(len_lhs - len_rhs, -1, -1):  # O(n - k)
    ok = True
    if carry == 0:
        for j in range(len_rhs - 1, -1, -1):  # O(k)
            if res_rem.b[i + j] > rhs.b[j]:
                ok = True
                break
            elif res_rem.b[i + j] < rhs.b[j]:
                ok = False
                break

    if ok:
        res_div.b[i] = 1
        for j in range(0, len_rhs):  # O(k)
            res_rem.b[i + j] -= rhs.b[j]
            if res_rem.b[i + j] < 0:
                res_rem.b[i + j] += 2
                res_rem.b[i + j + 1] -= 1
    else:
        res_div.b[i] = 0
    carry = res_rem.b[i + len_rhs - 1]
