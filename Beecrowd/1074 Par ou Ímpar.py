casos = int(input())

c = 1
while c <= casos:

    numero = int(input())
    if numero == 0:
        print('NULL')
    elif numero % 2 == 1 and numero < 0 :
        print('ODD NEGATIVE')
    elif numero % 2 == 1 and numero > 0 :
        print('ODD POSITIVE')
    elif numero % 2 == 0 and numero < 0 :
        print('EVEN NEGATIVE')
    elif numero % 2 == 0 and numero > 0 :
        print('EVEN POSITIVE')  
    
    c +=1