soma = 0
def quantasletras():
    global soma
    frase = input("Qual é a frase? ")
    letra = input("Qual é a letra? ")
    for i in frase:
        if i == letra:
            soma += 1
    print(f"Nesta frase aparece {soma} vezes a letra ({letra}).")

quantasletrastem()
