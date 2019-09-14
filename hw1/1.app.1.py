def bit_len(n):
    """
    Return bit length of n.
    Time complexity: O(|n|)
    """
    result = 0
    while n > 0:
        n >>= 1
        result += 1

    return result


class Binary:
    def __init__(self, value=None):
        if isinstance(value, int):
            n_bits = bit_len(value)
            self.b = [0] * n_bits
            for i in range(n_bits):
                self.b[i] = value % 2
                value //= 2
        elif isinstance(value, list):
            self.b = value

    def __str__(self):
        integer = 0
        for num in self.b[::-1]:
            integer = integer << 1 | num
        return str(integer)

    def copy(self):
        result = Binary()
        result.b = self.b.copy()
        return result

    def len(self):
        return len(self.b)

    def add(self, rhs):
        if not isinstance(rhs, Binary):
            raise TypeError("rhs is not Binary")

        len_lhs, len_rhs = self.len(), rhs.len()

        result = []

        carry = 0

        for i in range(max(len_lhs, len_rhs)):
            s = 0
            if i < len_lhs:
                s += self.b[i]
            if i < len_rhs:
                s += rhs.b[i]
            result.append(s + carry)

            if result[-1] < 2:
                carry = 0
            else:
                carry = 1
                result[-1] -= 2

        if carry > 0:
            result.append(carry)

        return Binary(result)

    def _div_rem(self, rhs):
        if not isinstance(rhs, Binary):
            raise TypeError("rhs is not Binary")

        len_lhs, len_rhs = self.len(), rhs.len()

        res_div, res_rem = Binary(0), self.copy()

        res_div.b = [0] * (len_lhs - len_rhs + 1)

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

        while res_div.b and res_div.b[-1] == 0:
            res_div.b.pop()

        while res_rem.b and res_rem.b[-1] == 0:
            res_rem.b.pop()

        return res_div, res_rem

    def div(self, rhs):
        if not isinstance(rhs, Binary):
            raise TypeError("rhs is not Binary")

        return self._div_rem(rhs)[0]

    def rem(self, rhs):
        if not isinstance(rhs, Binary):
            raise TypeError("rhs is not Binary")

        return self._div_rem(rhs)[1]

    def greaterthan(self, rhs):
        if not isinstance(rhs, Binary):
            raise TypeError("rhs is not Binary")

        len_lhs, len_rhs = self.len(), rhs.len()

        if len_lhs != len_rhs:
            return len_lhs > len_rhs

        for i in range(len_rhs - 1, -1, -1):
            if self.b[i] != rhs.b[i]:
                return self.b[i] > rhs.b[i]

        return False

    def equals(self, rhs):
        if not isinstance(rhs, Binary):
            raise TypeError("rhs is not Binary")

        len_lhs, len_rhs = self.len(), rhs.len()

        if len_lhs != len_rhs:
            return False

        for i in range(len_rhs):
            if self.b[i] != rhs.b[i]:
                return False

        return True


def euclid(a, b):
    a, b = Binary(a), Binary(b)
    while b.greaterthan(Binary(0)):
        r = a.rem(b)  # so a = bu + r
        if r.equals(Binary(0)):
            return b
        s = b.rem(r)  # so b = rv + s
        a = r
        b = s
    return a


print(euclid(12, 8))
