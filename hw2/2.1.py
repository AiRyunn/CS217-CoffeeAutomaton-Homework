from random import shuffle

count = 0


def lessthan(a, b):
    global count
    count += 1
    return a < b


def greaterthan(a, b):
    global count
    count += 1
    return a > b


def find_min_and_max(array):
    n = len(array)
    mi, mx = None, None
    for i in range(0, n, 2):
        if not lessthan(array[i], array[i + 1]):
            # swap the pairs
            array[i], array[i + 1] = array[i + 1], array[i]
    for i in range(0, n, 2):
        if mi is None or lessthan(array[i], mi):
            mi = array[i]
        if mx is None or greaterthan(array[i + 1], mi):
            mx = array[i + 1]
    return mi, mx


n = 20
array = [i for i in range(n)]
shuffle(array)

print(f"array: {array}")

print(f"min and max: {find_min_and_max(array)}")
print(f"3 n / 2 - 2 = {3 * n // 2 - 2}")
print(f"number of comparisons: {count}")
