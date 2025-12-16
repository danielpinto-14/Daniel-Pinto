from time import sleep

def FogueteDois(foguete3):
    print(foguete3)
    sleep(1)
    
def Foguete():
    foguete3 = int(input("Qual é o número inicial da contagem? "))

    while True:
        if foguete3 == 0:
            print(f"O foguete foi lançado!!")
            break
        else:
            FogueteDois(foguete3)
            foguete3 -= 1
         
Foguete()
