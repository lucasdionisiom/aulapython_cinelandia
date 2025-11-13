#Crie uma uma funcao que receba o lado de um quadrado e retorne o valor da sua area ($A = lado^2$)
def quadrado(lado):
    #Usando o operaor de exponenciação (**)
    return lado ** 2

#interacao com o usuario 
medida_lado = float(input("Digite a medida do lado do quadrado:  "))

#Chamada a função e exibição do resultado 
area = quadrado (medida_lado)
print(f"A area do quadrado é: {area}")