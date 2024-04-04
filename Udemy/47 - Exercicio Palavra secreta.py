palavraSecreta = 'abc'
letraAcertadas = ' '
tentativas = 0

while True:
    letraChute = str(input())
    tentativas += 1

    if letraChute in palavraSecreta:
        letraAcertadas += letraChute
        
    palavraFormada = ''
    for letraSecreta in palavraSecreta:
        if letraSecreta in letraAcertadas:
            palavraFormada += letraSecreta
        else:
            palavraFormada+= '*'

    print(palavraFormada)

    if palavraFormada == palavraSecreta:
        print('Voce ganhou')
        print('Numero de tentativas: ',tentativas)
        break