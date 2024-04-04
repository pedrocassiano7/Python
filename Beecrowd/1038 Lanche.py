codigo = [1 ,2 ,3, 4, 5]
especificação = ['CachorroQuente', 'XSalada, XBacon, TorradaS, Refrigerante']
preco = [4, 4.5, 5, 2, 1.5]

codigoIten, qtd = input().split()
codigoIten = int(codigoIten) - 1
qtd = int(qtd)

total = qtd * preco[codigoIten]

print(f'Total: R$ {total:.2f}')