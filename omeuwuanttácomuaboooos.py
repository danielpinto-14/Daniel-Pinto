#Solicitando ao uzuário que insira um número
numero = int(input("Digite um número: "))
start = int(input("Em que número começar: "))
loop = int(input("De quanto em quanto: "))
#Exibindo todos os Números que antecedam o número fornecido
print(f"Os números que antecedecem {numero} são: ")
for i in range(start, numero, loop):
    print(i)
