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

def JogoCPU():

def JogoPlayer():

def LógicaJogo(jogadorum, jogadordois):

    jogadorum = []
    jogadordois = []

    while True:
        A1 = " "

        print("       |      |      | ")
        print(f" {A1} | {A2} | {A3} | ")
        print("       |      |      | ")
        print("="*11)
        print("       |      |      | ")
        print(f" {B1} | {B2} | {B3} | ")
        print("       |      |      | ")
        print("="*11)
        print("       |      |      | ")
        print(f" {C1} | {C2} | {C3} | ")
        print("       |      |      | ")

        input()




def Main():
    Cabeçalho("JOGO DO GALO")
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
            JogoPlayer()
        else:
            Sub_Cabeçalho("Escolha não válida")

Main()

        




Menu()

