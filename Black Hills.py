import os

def limpar():
    os.system("cls")

def Cabeçalho(texto):
    limpar()
    cumprimento = len(texto) + 6
    print()
    print("="*cumprimento + 2)
    print(f"|| {texto} ||")
    print("="*cumprimento + 2)
    print()

def Sub_Cabeçalho(texto):
    limpar()
    print()
    print(f"### {texto} ###")
    print()

def Menu():
    Cabeçalho("JOGO DO GALO")
    input("\nEnter para Iniciar")
    Sub_Cabeçalho("MENU")
    escolha = int(input("\n 1 - PLAYER VS. CPU \n 2 - PLAYER VS. PLAYER \n 0 - QUIT GAME \n"))
    return escolha