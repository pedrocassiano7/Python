p1, p2, p3, p4 = input().split()
p1 = float(p1)
p2 = float(p2)
p3 = float(p3)
p4 = float(p4)

media = (p1 * 0.2) + (p2 * 0.3) + (p3 * 0.4) + (p4 * 0.1)

print(f'Media: {media}')

if media >= 7:
    print('Aluno aprovado.')
elif 5 <= media < 7:
    print('Aluno em exame.')
    pr = float(input())
    print(f'Nota do exame: {pr:.1f}')
    mediafinal = (pr + media) / 2

    if mediafinal >= 5:
        print('Aluno aprovado.')
        print(f'Media final: {mediafinal:.1f}')
    else:
        print('Aluno reprovado.')
        print(f'Media final: {mediafinal:.1f}')
else:
    print('Aluno reprovado.')