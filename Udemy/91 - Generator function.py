# Introdução às Generator functions em Python
# generator = (n for n in (1000000))

def generator(min=0, max = 100):
    while True:
        yield min
        min+=1
        if n>max:
            break

gen = generator(min = 500, max = 1000)
for n in gen:
    print(n)