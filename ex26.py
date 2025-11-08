'''desenvolva um codigo python que leia 5 numeros 
e diga se cada numero ao momento que for lido se é par ou impar'''
for i in range(1,6):
    x=int(input("digite um numero"))
    if x % 2 == 0:
        print(f"{x} é par")
    else:
        print(f"{x} é impar")

