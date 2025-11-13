'''crie a função que receba dois numeros e retorne o maior deles.'''
def numeros (a, b):
    if a > b:
        return a
    else:
        return b

# interaçao com usario 
a= int(input("Digite um numero inteiro:  "))
b= int(input("Digite um numero inteiro:  "))
mensagem= numeros(a, b)
print(f"o numero maior é {mensagem}")