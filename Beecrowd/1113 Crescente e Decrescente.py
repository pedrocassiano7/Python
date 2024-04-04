while True:
    m, n = input().split()
    m = int(m)
    n = int(n)

    if m < n:
        print('Crescente')
    elif m > n:
        print('Decrescente')
    elif m == n:
        break