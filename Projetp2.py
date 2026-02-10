#projeto

import os

def Limpar():
    os.system("cls")

def Cabeçalho(texto):
    Limpar()
    cumprimento = len(texto) + 6
    print()
    print("="*cumprimento)
    print(f"|| {texto} ||")
    print("="*cumprimento)
    print()

def Sub_Cabeçalho(texto2):
    print()
    print(f"(=( {texto2} )=)")
    print()

def Menu():
    Cabeçalho("JOGO DE LUTA")
    Sub_Cabeçalho("MENU")
    print("\n 1 - PLAYER VS. CPU \n 2 - PLAYER 1 VS. PLAYER 2 \n 0 - QUIT GAME \n")
    escolha = int(input("Escolha: "))
    return escolha

def Main():
    Cabeçalho("JOGO DE LUTA")
    Sub_Cabeçalho("MENU")
    input("\n\nPrime Start para começar (enter)") 
    while True:
        escolha = Menu()
        if escolha == 0:
            print("desligou".upper())
            break
        elif escolha == 1:
            while True:

                listaPersonagens = ["BLANKA", "RYU", "DALSHIM", "SONGOKU"]

                Cabeçalho("Escolher Personagem de Player1")

                print(listaPersonagens)
                listaNumberPersonagens = [1, 2, 3, 4]
                print("\nEscolhe o personagem, de 1 a 4, Player1")
                personagemPlayer = int(input("\nEscolha: "))
                personagemPlayer -= 1

                if personagemPlayer in listaNumberPersonagens:
                    print("PLAYER 1 pronto!") 

                    input("Enter P/ Continuar")
                    Cabeçalho("Escolher Personagem de CPU")
                    print(listaPersonagens)
                    print("\nEscolhe o personagem, de 1 a 4, CPU")
                    personagemCPU = int(input("\nEscolha: "))

                    if personagemCPU in listaNumberPersonagens:
                        print("CPU pronto!")    
                        break                
                    else:
                        print("Erro!")
                        input("Enter P/ Continuar")

                        return              
                else:
                    print("Erro!")
                    input("Enter P/ Continuar")

                input("Enter P/ Continuar")

        elif escolha == 2:
            while True:

                listaPersonagens = ["BLANKA", "RYU", "DALSHIM", "SONGOKU"]

                Cabeçalho("Escolher Personagem de Player1")

                print(listaPersonagens)
                listaNumberPersonagens = [1, 2, 3, 4]
                print("\nEscolhe o personagem, de 1 a 4, Player1")
                personagemPlayer = int(input("\nEscolha: "))
                personagemPlayer -= 1

                if personagemPlayer in listaNumberPersonagens:
                    print("PLAYER 1 pronto!") 

                    input("Enter P/ Continuar")
                    Cabeçalho("Escolher Personagem de PLAYER 2")
                    print(listaPersonagens)
                    print("\nEscolhe o personagem, de 1 a 4, PLAYER 2")
                    personagemP2 = int(input("\nEscolha: "))

                    if personagemP2 in listaNumberPersonagens:
                        print("PLAYER 2 pronto!")    
                        break                
                    else:
                        print("Erro!")
                        input("Enter P/ Continuar")

                        return              
                else:
                    print("Erro!")
                    input("Enter P/ Continuar")

                input("Enter P/ Continuar")

player1 = 30
cpu = 30

def LutaA(soco):
    global player1
    player1 = player1 - soco
    print()

def LutaA(soco):
    global cpu
    cpu = cpu - soco
    print()

def Soco():
    soco = (5)
    return soco

def LutaA():
    global player1
    global cpu

player1 = 30
player2 = 30

def LutaB(soco):
    global player1
    player1 = player1 - soco
    print()

def LutaB(soco):
    global player2
    player2 = player2 - soco
    print()

def Soco():
    soco = (5)
    return soco

def LutaB():
    global player1
    global player2

Menu()

Main()

LutaA()

LutaB()