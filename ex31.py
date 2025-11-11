'''desenvolva um codigo py com while em que o usuario digita o numero e irá mostrar a tabuada deste numero'''
numero=int(input("Digite um numero"))
i=1
while i <= 10:
    resultado = numero * i
    print(f"{numero}x{i}={resultado}")
    i += 1

