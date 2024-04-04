perguntas = [
    {
        'Pergunta': 'Quanto é 2+2',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },

    {
        'Pergunta': 'Quanto é 5*5',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },

    {
        'Pergunta': 'Quanto e 10/2',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },

    {
        'Pergunta': 'Qual a metade de 1 + 1',
        'Opções': ['1', '2.5', '1.5', '0'],
        'Resposta': '1.5',
    },
]

hits = 0

for pergunta in perguntas:
    print(f'Pergunta:', pergunta['Pergunta'])
    print('')
    print('Opções:')

    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i})', opcao)
    
    print('')

    option_select = str(input('Escolha uma opção: '))

    for numero in range(0,4):
        if option_select == str(numero):
            option_select = pergunta['Opções'][numero]

    
    if pergunta['Resposta'] ==  option_select:
        print("Acertou ✅")
        hits += 1
        
    else:
        print("Errou ❌")
    
    print('')
    print('')

print(f'Você acertou {hits} de {len(perguntas)} perguntas')