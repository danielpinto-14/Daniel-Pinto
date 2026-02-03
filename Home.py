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
    Cabeçalho("JOGO DO PEDRA, PAPEL & TESOURA")
    input("\nEnter para Iniciar")
    Sub_Cabeçalho("MENU")
    escolha = int(input("\n 1 - PLAYER VS. CPU \n 2 - PLAYER VS. PLAYER \n 0 - QUIT GAME \n"))
    return escolha

def JogoCPU():

LógicaJogo(jogadorum, jogadordois):

items = ["Pedra", "Papel", "Tesoura"]
print(f"O jogador um escolha")
if jogadorum == 0:
        if jogadordois == 0:
escolha = int(input("\n Enter para Continuar"))

def Main():
    Cabeçalho("JOGO DO PEDRA, PAPEL & TESOURA")
    input("\n\nEnter para iniciar") 
    while True:
        escolha = Menu
        if escolha == 0:
            limpar()
            print(" # Sayonara # ".upper)
            break
        elif escolha == 1:
            JogoCPU()
        elif escolha == 2:
            JogoPLAYER()
        else:
            Sub_Cabeçalho("Escolha não válida")

Main()

        




Menu()