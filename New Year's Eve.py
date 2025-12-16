from random import randint

lutadorA = 30
lutadorB = 30

def LutaDeBoxA(soco):
    global lutadorB
    lutadorB = lutadorB - soco
    print()

def EscolhaDeDano(dano):
    if dano == "soco":
        print(f"O {lutadorA} levou um soco de poder {Soco()}!!")

def LutaDeBoxB(soco):
    global lutadorA
    lutadorA = lutadorA - soco
    print()

def Soco():
    soco = randint(1, 3)
    return soco

def Pontapé():
    pontape = randint(2, 4)
    return pontape

def BolaDeFogo():
    boladefogo = randint(6, 9)
    return boladefogo

def Cabeçada():
    cabecada = randint(1, 4)
    return cabecada

def Kamehameha():
    kamehameha = randint(12, 18)
    return kamehameha

def VouChamarAMinhaMãe():
    vouchamaraminhamãe = randint(30)
    return vouchamaraminhamãe

def Luta():
    global lutadorA
    global lutadorB

    while True:
         if lutadorA and lutadorB > 0:
            dano = input("Qual o dano a aplicar? (soco/pontape/bola de fogo/ cabecada/ kamehameha/ vou chamar a minha mae): ")
            if dano == "soco":

                print(f"O {lutadorA} levou um soco de poder {Soco()}!!")

        
        if soco:
            print(f"O {lutador} levou um soco de poder {soco}!!")
        
        elif pontape:
            print(f"O {lutador} levou um pontape de poder {pontape}!!")

        elif boladefogo:
            print(f"O {lutador} levou uma bola de fogo de poder {boladefogo}!!")

        elif cabecada:
            print(f"O {lutador} levou uma cabeçada de poder {cabecada}!!")

        elif kamehameha:
            print(f"O {lutador} levou um kamehameha de poder {kamehameha}!!")

        elif vouchamarainhamãe:
            print(f"O {lutador} ouviu um {vouchamaraminhamãe}, ele ficou cheio de medo e perdeu o combate!!")

        else:






