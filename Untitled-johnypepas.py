#ytre:
ordenado = float(input("Quanto é o teu ordenado? "))
if ordenado<500:
    print("O teu reajuste será de 15%")
    reajuste = 15
elif ordenado<1000:
    print("O teu reajuste será de 10%")
    reajuste = 10
else:
    print("O teu reajuste será de 5%")
    reajuste = 5
valor_aumento = (ordenado * reajuste) / 100
novo_ordenado = ordenado + valor_aumento
print(f"\n0 O reajuste será de /{reajuste}%")
print(f"O aumento será de {valor_aumento:.2f}€")
print(f"O novo salário passará para {novo_ordenado:.2f}€")