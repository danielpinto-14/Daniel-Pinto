inicio = int(input("Escolhe o primeiro número: "))
final = int(input("Escolhe o ultímo número: "))
soma = 0

for n1 in range (inicio, final +1):
    soma += n1
    if n1 == inicio:
        print(f"[ {n1}", end = " + ")

    elif n1 == final:
        print(n1, end = " ]")

    else:
        print(n1, end = " + ")  

print()
print(f"\nA Soma de todos os números de {inicio} até {final} é {soma}\n")




