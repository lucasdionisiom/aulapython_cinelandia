Valor1=int(input("Digite um valor: "))
Valor2=int(input("Digite outro valor: "))
Valor3=int(input("Digite outro valor: "))
if(Valor1 > Valor2 and Valor1 > Valor3):
    print(f"{Valor1} é o valor maior")
elif(Valor2 >= Valor1 and Valor2 > Valor3 ):
    print(f"{Valor2} é o valor maior")
else:
    print(f"{Valor3} é o valor maior")