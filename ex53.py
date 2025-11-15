#Leia duas notas, calcule a média e trate erros de entrada (valor inválido ou divisão incorreta.)
def calcular_media ():
    #Funcao sem receber parametros
    try:
        nota1=float(input("Digite a primeira nota (0 a 10)"))
        nota2=float(input("Digite a segunda nota (0 a 10)"))
        media = (nota1+nota2) / 2
    except ValueError:
        print("Erro digitar apenas numeros validos!")
    else:
        print(f"Media calculada: {media:.2f}")
    finally:
        print("Fim do calculo de media.")
calcular_media()