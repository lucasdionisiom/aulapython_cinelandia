''' Desenvolva um codigo python que leia um cargo de funcionario, de acordo com o cargo mostre o salaio vide tabela abaixo.
caixa - 1500
vendedor - 2400
genrente - 4000
de acordo com os slarios acima. calculae: 
inss = 12% sobre o salario
irrf se o salario for maior que 2000 e o irrf sera de 14% sobre o salario senao de 8%
salario final = salario - irrf - inss'''
#Tabela de salários base
cargo=input("Digite seu cargo (caixa, vendedor ou gerente)").lower()
if (cargo=="caixa"):
    sal=1500
elif (cargo=="vendedor"):
    sal=2400
elif (cargo=="gerente"):
    sal=4000
else:
    sal=0
    print("cargo nao existe")
inss = sal * 0.12
if (sal > 2000):
    irrf = sal * 0.14 
else:
    irrf = sal * 0.08
salariofinal= sal - inss - irrf 
print(f"seu salário é {sal}, e seu salario finl é {salariofinal}")
print(f"seus descontos foram de inss {inss} e irrf {irrf}")
