#
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