numero = int(input())

c = 1
while c <= 10000:
    if c % numero == 2:
        print(c)
    c += 1