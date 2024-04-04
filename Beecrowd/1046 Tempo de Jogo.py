horaInicial, horaFinal = input().split()
horaInicial = int(horaInicial)
horaFinal = int(horaFinal)

tempoDeJogo = horaFinal - horaInicial

if horaInicial >= horaFinal:
    tempoDeJogo += 24

print(f'O JOGO DUROU {tempoDeJogo} HORA(S)')