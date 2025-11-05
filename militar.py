'''Estudo de caso
voce foi contratado pelo exercito brasieiro para desenvolver um sistema de alistamento militar,
onde se le o ano e nascimento e o GeneratorExit
o sistma irá calcular a idade, se a idade for maior igual a 18 e o sexo masculino ele estrá apto a se alistar, senao nao apto'''
anonasc=int(input("Digite o ano de nascimento"))
genero=input("Digite o sexo M ou F").upper()
#print(anonasc)
#print(genero
idade=2025-anonasc
if (idade >=18 and genero == "M"):
    print("apto a se alistar")
else:
    print("não apto")