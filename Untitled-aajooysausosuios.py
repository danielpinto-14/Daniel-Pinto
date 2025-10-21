#wertyuiop:
distancia = float(input("Insira s distÂncia da viagem em quilómetros: "))
print("\nEscolha o meio de transporte: ")
print("1. Carro (0.50 euros por km)")
print("2. Comboio (0.30 euros por km)")
print("3. Avião (1,00 euros por km)")
meio_transporte = int(input("Digite o número correspondente ao meio de transporte: "))
if meio_transporte == 1:
    preco_por_km = 0.50
elif meio_transporte == 2:
    preco_por_km = 0.30
elif meio_transporte == 3:
    preco_por_km = 1.00
else:
    preco_por_km = 0
    print("Opção inválida. O custo não será calculado correctamente")

#Solicitar a quantidade de pessoas na viagem
quantidade_pessoas = int(input("\nInsira a quantidade de pessoas na viagem: "))

#Calcular o custo total da viagem
custo_total = distancia * preco_por_km * quantidade_pessoas

#Exibir o custo total da viagem
print("\nResumo da Viagem: ")
print("Distância: " + str (distancia) + "km")
print("Preço por km: €" + str(distancia) + "km")
print("Quantidade de pessoas: " + str(quantidade_pessoas))
print("Custo Total da Viagem: €" + str(custo_total))
