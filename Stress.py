def encontrarletra ():   
    frase = input("Qual é a frase? ")
    letra = input("Qual letra quer procurar? ")

    if letra in frase:
        print(f"A Letra {letra} está na frase ")
    else:
        print(f"A Letra {letra} não está na frase")

encontrarletra()


