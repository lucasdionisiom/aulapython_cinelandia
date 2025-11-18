import pandas as pd

# Listas vazias para armazenar os dados
cargos = []
salarios = []

#Quantos registros o usuario vai informar
qtd = int(input("Quantos cargos deseja cadastrar?"))

# Coleta de dados 
for i in range(qtd):
    print(f"Cadastro {i+1}:")
    cargo = input("Digite o cargo: ")
    salario = float(input("Digite o salário: "))

    cargos.append(cargo)
    salarios.append(salario)

#Criação do DataFrame
dados = {'cargos': cargos, 'salarios': salarios}
dados_bi = pd.DataFrame(dados)

#Exibição do DataFrame final
print("Tabela de Cargos e Salários:")
print(dados_bi)