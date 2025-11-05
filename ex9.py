#desenvolver um código python que leia 2 nomes
nome1=input("Qual o seu nome? ")
nome2=input("Digite o sobrenome ")
nome1=nome1.upper()
nome2=nome2.upper()
if (nome1 == "SENAC" or nome2=="Cinelândia"):
    print(f"Seja bem vindo ao, {nome1} {nome2}!")
else:
    print("Não é Senac.")