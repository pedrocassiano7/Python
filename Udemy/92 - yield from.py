# Yield from

def gen1():
    yield 1
    yield 2
    yield 3

def gen2():
    yield from gen1()
    yield 4
    yield 5
    yield 6 

gen1()
gen2()

for n in gen2():
    print(n)