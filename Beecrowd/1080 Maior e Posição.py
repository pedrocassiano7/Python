cont = 1
p = 1
numeroAntigo = 0
posicao = 0

while cont <= 100:
    numeroAtual = int(input())
    if numeroAntigo <= numeroAtual:
        numeroAntigo = numeroAtual
        posicao = p
    p += 1   
    cont +=1

print(numeroAntigo)
print(posicao)