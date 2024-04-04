palavra1 = str(input())
palavra2 = str(input())
palavra3 = str(input())

if palavra1 == 'vertebrado':
    if palavra2 == 'ave':
        if palavra3 == 'carnivoro':
            print('aguia')
        else: # onivoro
            print('pomba')
    else: #mamifero
        if palavra3 == 'onivoro':
            print('homem')
        else: #herbivoro
            print('vaca')
else: #invertebrado
    if palavra2 == 'inseto':
        if palavra3 == 'hematofago':
            print('pulga')
        else: # onivoro
            print('lagarta')
    else: #mamifero
        if palavra3 == 'hematofago':
            print('sanguessuga')
        else: #herbivoro
            print('minhoca')