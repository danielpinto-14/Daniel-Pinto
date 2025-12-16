def Conversacaofhrcel(temperatura):
    return ((temperatura - 32) * (5/9))

def Temperatura():
    valorTemperatura = float(input("Escreve a temperatura"))

    temperatura = Conversacaofhrcel(valorTemperatura)

print(f"\nTemperatura = {Temperatura:.2f}ºC")

for i in range(1, 71): 
    Temperatura() 


            