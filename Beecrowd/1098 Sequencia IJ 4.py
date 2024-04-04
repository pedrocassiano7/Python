i = float(0)
j1 = 10
j2 = 20
j3 = 30

while i <= 20:
    if i % 10 == 0:
        print(f'I={i/10:.0f} J={j1/10:.0f}')
        print(f'I={i/10:.0f} J={j2/10:.0f}')
        print(f'I={i/10:.0f} J={j3/10:.0f}')
    else:
        print(f'I={i/10:.1f} J={j1/10:.1f}')
        print(f'I={i/10:.1f} J={j2/10:.1f}')
        print(f'I={i/10:.1f} J={j3/10:.1f}')
    j1 += 2
    j2 += 2
    j3 += 2
    i += 2