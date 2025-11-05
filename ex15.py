ano=int(input("Qual ano do seu nascimento?"))
genero=input("Qual seu genero (M/F?)?").upper()
if(ano<2007 and genero == "M"):
  print("Você está apto")
else:
  print("Você não está apto.")