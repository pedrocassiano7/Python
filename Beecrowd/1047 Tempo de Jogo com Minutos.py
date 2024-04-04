horaInicial, minutoInicial, horaFinal, minutoFinal = input().split()
horaInicial = int(horaInicial)
minutoInicial = int(minutoInicial)
horaFinal = int(horaFinal)
minutoFinal = int(minutoFinal)

horas = horaFinal - horaInicial
minutos = minutoFinal - minutoInicial

if horas <= 0:
    horas += 24
           
if minutos < 0:
    minutos += 60
    horas -= 1

if horas == 24 and minutoInicial < minutoFinal:
    horas -= 24

print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')