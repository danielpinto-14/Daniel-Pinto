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

def Menu():
    Cabeçalho("JOGO DE LUTA")
    print("\n 1 - PLAYER VS. CPU \n 2 - PLAYER 1 VS. PLAYER 2 \n 0 - QUIT GAME \n")
    escolha = int(input("Escolha: "))
    return escolha


def Main():
    Cabeçalho("JOGO DE LUTA")
    input("\n\nPrime Start para começar (enter)") 
    while True:
        escolha = Menu()
        if escolha == 0:
            print("desligou".upper())
            break
        elif escolha == 1:
            while True:

                listaPersonagens = ["Frankenstein", "Mickey", "Pacman", "Hulk"]

                Cabeçalho("Escolher Personagem de Player1")

                print(listaPersonagens)
                listaNumberPersonagens = [0, 1, 2, 3]
                print("\nEscolhe o personagem, de 0 a 3, Player1")
                personagemPlayer = int(input("\nEscolha: "))
                personagemPlayer -= 1

                if personagemPlayer in listaNumberPersonagens:
                    print("PLAYER 1 pronto!") 

                    input("Enter P/ Continuar")
                    Cabeçalho("Escolher Personagem de CPU")
                    print(listaPersonagens)
                    print("\nEscolhe o personagem, de 0 a 3, CPU")
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

                listaPersonagens = ["BLANKA", "RYU", "SONGOKU", "SEIYA"]

                Cabeçalho("Escolher Personagem de Player1")

                print(listaPersonagens)
                listaNumberPersonagens = [0, 1, 2, 3]
                print("\nEscolhe o personagem, de 0 a 3, Player1")
                personagemPlayer = int(input("\nEscolha: "))
                personagemPlayer -= 1

                if personagemPlayer in listaNumberPersonagens:
                    print("PLAYER 1 pronto!") 

                    input("Enter P/ Continuar")
                    Cabeçalho("Escolher Personagem de PLAYER 2")
                    print(listaPersonagens)
                    print("\nEscolhe o personagem, de 0 a 3, PLAYER 2")
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
CPU = 30

def Luta(soco):
    global player1
    player1 = player1 - soco
    print()

def LutaDeBoxB(soco):
    global CPU
    CPU = CPU - soco
    print()

def Soco():
    soco = (5)
    return soco

player1 = 30
player2 = 30

def Luta(soco):
    global player1
    player1 = player1 - soco
    print()

def LutaDeBoxB(soco):
    global player2
    player2 = player2 - soco
    print()

def Soco():
    soco = (5)
    return soco




















Main()
