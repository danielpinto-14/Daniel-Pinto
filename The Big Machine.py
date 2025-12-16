from time import sleep

def FogueteDois(foguete3):
    print(foguete3)
    sleep(1)
    
def Foguete():
    foguete3 = int(input("Qual é o número inicial da contagem? "))

    for i in range(Foguete):
        Foguete(foguete3)
        contador -= 1
        if contador == 0:
            print("O foguete foi lançado!!")
            break

Foguete()
