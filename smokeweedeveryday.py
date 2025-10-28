#EEE
nota = int(input("Qual é a nota? "))
match nota:
    case 20:
       avaliacao = "Excelente"
    case 18:
        avaliacao = "Muito bom"
    case _:
        avaliacao = "Nota não Reconhecida"
print("a avaliação é: ", avaliacao)