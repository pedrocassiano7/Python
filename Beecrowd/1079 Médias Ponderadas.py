casos = int(input())

cont = 1
while cont <= casos:

    a, b, c = input().split()
    a = float(a)
    b = float(b)
    c = float(c)

    mediaPonderada = ((a*2) + (b*3) + (c*5))/10
    print(f'{mediaPonderada:.1f}')
    
    cont +=1