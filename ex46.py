#6) Crie uma função que receba um valor em metros e retorne o valor correspondente em centímetros ($1m = 100cm$).
def metros_para_cm(metros):
    return metros * 100

# Interação com o usuário
valor_metros = float(input("Digite o valor em metros: "))

# Chamada da função e exibição do resultado
valor_cm = metros_para_cm(valor_metros)
print(f"{valor_metros} metros é igual a {valor_cm} centímetros.")