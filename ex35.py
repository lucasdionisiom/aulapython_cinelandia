nota=0
while nota >= 0 and nota <= 10:
    try:
        nota=int(input("Digite um numero entre 0 e 10: "))
        print(f"Nota válida: {nota}")
    except ValueError:
        print("Entrada Invalida. Digite um numero inteiro.")
print(f"Nota invalida: {nota}")