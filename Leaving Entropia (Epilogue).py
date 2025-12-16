from random import randint 

def pensação():
    numeroSecreto = randint(0, 100)

    while True:
        numero = int(input("Qual é o nº? "))
        if numeroSecreto == numero:
            print(f"o número é {numero}")
            break
        elif numeroSecreto > numero:
            print("o número é maior")
        elif numeroSecreto < numero:
            print("o número é menor")
            

pensação()

