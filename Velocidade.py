#Velocidade
velocidade = int(input("Quanto é a velocidade? "))

limite_de_velocidade = 80
valor_acima_de_120 = 4
valor_por_km = 2

if velocidade > limite_de_velocidade:
    excesso_de_velocidade = velocidade - limite_de_velocidade
    multa = excesso_de_velocidade * valor_por_km
    mensagem = f"Está acima do limite permitido. A multa foi gerada no valor de {multa:.2f} euros."
elif valor_acima_de_120 < limite_de_velocidade:
    multa = limite_de_velocidade * valor_por_km
    mensagem = f"Está um pouco acima do limite peremitido. A multa foi gerada no valor de {multa:.2f} euros."
else:
    mensagem = "Está dentro do limite. Boa viagem!"

print(mensagem)

