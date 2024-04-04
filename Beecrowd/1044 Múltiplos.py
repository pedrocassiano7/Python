a, b = input().split()
a = int(a)
b = int(b)

lista = [a, b]
organizar = sorted(lista)

if organizar[1] % organizar[0] == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')