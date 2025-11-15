# 7)Crie uma função que receba três notas e retorne a média aritmética delas.
def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

# Interação com o usuário
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

# Chamada da função e exibição do resultado
media_final = calcular_media(n1, n2, n3)
# O round(numero, 2) arredonda o resultado para 2 casas decimais
print(f"A média das notas é: {round(media_final, 2)}")