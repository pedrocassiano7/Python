senha = 2002

while True:
    lerSenha = int(input())
    if lerSenha != senha:
        print('Senha Invalida')
    else:
        print('Acesso Permitido')
        break
