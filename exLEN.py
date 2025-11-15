# Crie uma função que receba uma palavra (string) e retorne o número de letras que ela contém.

def contar_letras(palavra):
    # A função nativa len() retorna o comprimento (número de caracteres) da string.
    return len(palavra)

# Exemplo de utilização
palavra_digitada = "Exemplo"
num_letras = contar_letras(palavra_digitada)

print(f"A palavra '{palavra_digitada}' tem {num_letras} letras.")