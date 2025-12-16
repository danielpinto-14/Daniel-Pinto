def soma():
    resultado = primeirovalor + segundovalor
    return resultado

def subtração():
    resultado = primeirovalor - segundovalor
    return resultado

def divisão():
    resultado = primeirovalor / segundovalor
    return resultado

def multiplicação():
    resultado = primeirovalor * segundovalor
    return resultado



def cabecalho(texto):
    print()
    print("=" * 17)
    print(f"|| {texto} ||")
    print("=" * 17)
    print()

def calculadora():
    global primeirovalor
    global segundovalor

    while True:
        cabecalho("calculadora")
        print(" 1 - Soma\n 2 - Subtrair\n 3 - Dividir\n 4 - Multiplicar\n 0 - Sair")
        print()
        escolha = int(input("Qual sua escolha? "))
        print()
        if escolha == 0:
            break
        else:
            primeirovalor = float(input("Entre com o valor de A: "))
            segundovalor = float(input("Entre com o valor de B: "))
            if escolha == 1:
                resultado = soma()
            elif escolha == 2:
                resultado == subtração()
            elif escolha == 3:
                if segundovalor != 0.0:
                    resultado = divisão()
                else:
                    print("\nO segundo valor tem de ser diferente de 0.\n")
                    input("\nEnter para terminar")
                    return
            elif escolha == 4:
                resultado = multiplicação
            resultado == multiplicação()

        print(f"\nO resultado da conta é {resultado:.2f}")
        input("\nEnter para terminar")
        
calculadora()




