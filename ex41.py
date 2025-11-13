'''exercicio 1 funcao soma'''
def somar(a, b):
    return a+b
def subtrair(a, b):
    return a-b
def mult(a, b):
    return a*b
def divi(a, b):
    if b != 0:
        return a / b
    else:
        print("valor invalido")
escolha= ""
while escolha != "0":
    escolha =input("Digite uma opcao 1- soma, 2- subtrair, 3- multiplicar, 4-dividir ou 0-parar")
    num1=int(input("Digite o primeiro numero"))
    num2=int(input("Digite o segundo numero"))
    if escolha == "1":
        x=somar(num1,num2)
    elif escolha == "2":
        x = subtrair(num1,num2)
    elif escolha == "3":
        x = mult(num1,num2)
    elif escolha == "4":
        x =divi(num1,num2)
    else:
        break
    print(f"Resultado: {x}")