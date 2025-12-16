import random

numerosSorteados = []
numerosPares = []
somaPares = 0
soma = 0

def geradordenºsaleatorios():

    for i in range(1, 11):
        numero = random.randint(1, 100)
        numerosSorteados.append(numero)

    print(f"Os números sorteados foram: {numerosSorteados}")

def somadosnumerospares():

    global somaPares

    for numero in numerosSorteados:
        if numero % 2 == 0:
            numerosPares.append(numero)
            somaPares += numero

    print(f"Os números pares são: {numerosPares}")
    print(f"A soma dos valores pares na lista {numerosSorteados} é {somaPares}")

def somadetodosaleatorios():

    global soma

    for numero in numerosSorteados:
        soma += numero

    print(f"A soma dos valores na lista é: {soma}")

def somatodosnumeros():
    global soma
    soma += somaPares

    print(f"A soma dos valores nas lista + os Pares na lista é: {soma}")


geradordenºsaleatorios()
somadetodosaleatorios()
somadosnumerospares()
somatodosnumeros()
ç