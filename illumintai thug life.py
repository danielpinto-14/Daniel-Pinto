#escreva um conversor de moedas de euros para reais Brasileiros e bath Thailandeses
euro = float(input("Quantos euros você deseja converter? "))
print()
print("""Qual moeda deseja converter:
     [0] Real Brasileiro 
     [1] Bath Tailandeses
     [2] Sucre""")
moeda = int(input("Escolha a sua opção: "))
real = 5.32 * euro
bath_tailandeses = 31.10 * euro
sucre = 29700 * euro
print()
if moeda==0:
     print("Isso lhe dará", real, "em Reais Brasileiros")
elif moeda==2:
     print("Isso lhe dará", sucre, "em Sucres do Equador")
else:
     print("Isso lhe dará", bath_tailandeses, "em bath tailandeses")
