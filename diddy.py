maior = 0
menor = 0

for contador in range (1, 6):
    peso = float(input(f"\nEntre com o {contador}º peso:  "))

    print(f"\nO peso introduzido foi: {peso:.2f}kg")
    input("\nCarrega Enter para Continuar")

    #Se o Contador for a primeira vez: Maior e Menor = Peso
    if contador == 1:
        maior = menor = peso
    #Se o Peso for maior que maior, então maior é Igual ao peso
    if peso > maior:
        maior = peso
    #Se o Peso for menor que menor, então menor é igual ao peso
    if peso < menor:
        menor = peso

print()
print(f"O número maior é {maior:.2f}")
print(f"O número menor é {menor:.2f}")

