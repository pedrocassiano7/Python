casos = int(input())

c = 1
coelhos = 0
ratos = 0
sapos = 0
percentualC = 0
percentualR = 0
percentualS = 0

while c <= casos:
    
    quantidade, string = input().split()
    quantidade = int(quantidade)
    string = str(string)

    if string == 'C':
        coelhos += quantidade
    if string == 'R':
        ratos += quantidade 
    if string == 'S':
        sapos += quantidade 
    
    c += 1

total = coelhos + ratos + sapos
percentualC = (coelhos / total) * 100
percentualR = (ratos / total) * 100
percentualS = (sapos / total) * 100

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')
print(f'Percentual de coelhos: {percentualC:.2f} %')
print(f'Percentual de ratos: {percentualR:.2f} %')
print(f'Percentual de sapos: {percentualS:.2f} %')