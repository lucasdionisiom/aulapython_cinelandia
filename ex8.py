#codigo python que verifica se um nome é SENAC
nome=input("Qual o seu nome")
sobrenome=input("digite o sobrenome")
nome=nome.upper()
sobrenome=sobrenome.upper()
if (nome == "SENAC" and sobrenome=="SANTA LUZIA"):
    print(f"seja bem vindo {nome} {sobrenome}")
else:
    print("não é senac")
