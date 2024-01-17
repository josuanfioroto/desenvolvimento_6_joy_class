nome = input("Nome completo: ")
print("Seu nome é "+ nome)

while True:
  nascimento = int(input("Ano do seu nascimento: "))
  print("Sua idade em 2024 será" , 2024 - nascimento)


  if nascimento < 1922 or nascimento > 2024:
    print("Informar sua Data de nascimento, por favor.")

  else:
    break
