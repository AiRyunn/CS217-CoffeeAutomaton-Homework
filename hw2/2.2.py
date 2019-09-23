def exercise_2(a, n):       #a is the array, and n is the size
    if n  == 1:
        return [a[0], a[0]]
    elif a[0] < a[1]:       #1 comparison
        max = a[1]
        min = a[0]
    else:
        max = a[0]
        min = a[1]
    for i in range(1, n/2): #3 comparisons for each cycle
        if a[2*i] < a[2*i+1]:
            l = a[2*i]
            r = a[2*i+1]
        else:
            l = a[2*i+1]
            r = a[2*i]
        if l < min:
            min = l
        if r > max:
            max = r

    return [max, min]
