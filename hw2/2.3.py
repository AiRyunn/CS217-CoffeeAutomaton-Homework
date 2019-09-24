def exercise_3(a, n, k):                         #a is the array, and n is the size n = 2^k
    l = np.zeros(n,k)
    b = np.zeros(n)
    for i in range(0,n):
        b[i] = i
    m = n/2
    for i in range(0,k-1):                       #2^(k-i-1) comparisons
        for j in range(0, m):
            if a[ b[j] ] < a[ b[j+1] ]:
                l[ b[j+1] ].append( b[j] )
                b.pop(j)
            else:
                l[ b[j] ].append( b[j+1] )
                b.pop(j+1)
    m = m / 2
    if a[ b[0] ] < a[ b[1] ]:                     #1 comparison
        max = a[ b[1] ]
        second = a[ b[0] ]
        compare = l[ b[1] ]
    else:
        max = a[ b[0] ]
        second = a[ b[1] ]
        compare = l[ b[0] ]
    for i in range(0,k):                          #k comparisons
        if a[ compare[i] ] > second:
            second = a [ compare[i] ]
