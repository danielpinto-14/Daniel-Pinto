paises = ["Portugal", "França", "Reino Unido", "Itália", "Noruega", "Suécia", "Alemanha", "Dinamarca"]
while True:
   pais = input("Qual país é? ")

   if pais in paises:
        print("País encontrado")
        break
   else:
        print("País não encontrado")
        