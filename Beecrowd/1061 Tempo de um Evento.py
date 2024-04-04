s, diaI = input().split()
diaI = int(diaI)

horasI, s, minutosI, s, segundosI = input().split()

horasI = int(horasI)
minutosI = int(minutosI)
segundosI = int(segundosI)

s, diaF = input().split()
diaF = int(diaF)

horasF, s, minutosF, s, segundosF = input().split()

horasF = int(horasF)
minutosF = int(minutosF)
segundosF = int(segundosF)

s = str(s)

segundos = segundosF - segundosI
minutos = minutosF - minutosI
horas = horasF - horasI
dias = diaF - diaI

if segundos < 0:
    segundos += 60
    minutos -= 1

if minutos < 0:
    minutos +=60
    horas -= 1

if horas < 0:
    horas += 24
    dias -= 1

print(dias, "dia(s)")
print(horas, 'hora(s)')
print(minutos, 'minuto(s)')
print(segundos, 'segundo(s)')