'''desenvolva um codigo Python usando while que digite um nome e imprima, só para o programa ao digitar sair em maiusculo'''
# != diferente
nome =""
while nome != "sair":
    nome=input("Digite um nome (ou SAIR em maiusculo para finalizar)").upper()
    if nome== "SAIR":
        print("Programa finalizado")
        break #sai do laço
    print(f"Nome digitado:{nome}")
    