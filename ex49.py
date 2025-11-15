#9)Crie uma função que receba um número e retorne o seu antecessor (o número menos um).
def antecessor(numero):
    return numero - 1

# Interação com o usuário
num = int(input("Digite um número inteiro: "))

# Chamada da função e exibição do resultado
ant = antecessor(num)
print(f"O antecessor de {num} é: {ant}")


