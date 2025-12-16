import random

numerosSorteados = []

def geradordenºsaleatorios():

    for i in range(1, 11):
        numero = random.randint(1, 100)
        numerosSorteados.append(numero)

    print(f"Os números sorteados foram: {numerosSorteados}")
    print()

geradordenºsaleatorios()

