numero = int(input())

meses = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

cont = 1
for mes in meses:
    if numero == cont:
        print(mes)
        break
    cont += 1
