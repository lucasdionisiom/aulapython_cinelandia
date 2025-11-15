#Crie uma função que receba uma palavra (string) e retorne o número de letras que ela contém.
vogais = "aeiouAEIO"
def contar_vogais(palavra):
    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador += 1
    return contador
l= contar_vogais(vogais)

print(f"A palavra '{vogais}' tem {l} letras.")