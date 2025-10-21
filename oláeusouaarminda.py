#ertyui:
distância = float(input("Qual foi a distância da viagem? "))
meio_transporte = int(input("Qual é o teu meio de transporte? "))
carro = 1
autocarro = 2
avião = 3
preco_por_km = float(input("Qual é o preço por km do meio de transporte? "))
quantidade_pessoas = int(input("Quantas pessoas vão viajar? "))
custo_total =  distância * preco_por_km * quantidade_pessoas
print("O custo foi de: ", custo_total)