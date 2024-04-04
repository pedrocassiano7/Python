ddd = [61, 71, 11, 21, 32, 19, 27, 31]
cidades = ['Brasilia', 'Salvador', 'Sao paulo', 'Rio de Janeiro', 'Juiz de Fora', 'Campinas', 'Vitoria', 'Belo Horizonte']

numero = int(input())

cont = 0
for cidade in cidades:
    if numero == ddd[cont]:
        print(cidade)
        break
    
    cont += 1

else:
    print('DDD nao cadastrado')
    
    