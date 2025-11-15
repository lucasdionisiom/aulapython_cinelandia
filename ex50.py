#Exercício: Cálculo do IMC
#Crie uma função que receba o peso (em quilogramas) e a altura (em metros) de uma pessoa e retorne o valor do IMC.

def calcular_imc(peso, altura):
  
    # Evita divisão por zero, caso a altura seja zero
    if altura <= 0:
        return "Erro: Altura inválida."

    # A altura é elevada ao quadrado (altura ** 2)
    imc = peso / (altura ** 2)
    return imc

# Interação com o usuário
# É importante usar float() para aceitar números decimais (como 1.75)
try:
    peso_usuario = float(input("Digite seu peso em kg (ex: 70.5): "))
    altura_usuario = float(input("Digite sua altura em metros (ex: 1.75): "))

    # Chamada da função
    imc_resultado = calcular_imc(peso_usuario, altura_usuario)

    # Exibição do resultado
    if isinstance(imc_resultado, str):
        # Se for string, é a mensagem de erro
        print(imc_resultado)
    else:
        # Arredonda o IMC para duas casas decimais para melhor leitura
        print(f"\nSeu peso: {peso_usuario} kg")
        print(f"Sua altura: {altura_usuario} m")
        print(f"O seu IMC é: {round(imc_resultado, 2)}")

except ValueError:
    print("\nErro: Por favor, digite apenas números válidos.")
