'''Crie uma funcao que receba um nome como argumento (string) e retorne uma mensagem de saudacao completa'''
#Resolucao do exercicio 2
def saudar(nome):
    return f"Olá, {nome}! Seja bem-vindo(a) ao mundo Python!"

# Interação com o usuario
nome_usuario = input("Digite seu nome: ")

#Chamda da função e exibição do resultado
mensagem= saudar(nome_usuario)
print(mensagem)