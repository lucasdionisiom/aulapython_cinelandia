#Crie uma função que receba um número e retorne True se for par e False se for ímpar.
# Resolução do Exercício 3
def ehpar (numero):
    # o operador % (modulo) retorna o resto da divisao. Se o resto por 2 for 0, é par.
    return numero % 2 == 0

# interaçao com usario 
num = int(input("Digite um numero inteiro:  "))

#Chamda da funçao e exibição do resultado
resultado = ehpar (num)

if resultado:
    print(f"O numero {num} é par.")
else:
    print(f"O numero {num} é impar")