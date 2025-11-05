'''
Uma loja de produtos tecnologicos te contratou para desenvolver um codigo da seguite forma:
(1)Leia um produto e de acordo com o produto verifique o preço. (Vide tabela abaixo)
(2)produtos-preço
mouse-10
teclado-20
memória-100
e (3)Leia ainda a quantidade de produtos comprados:
Calcule:
(4)total = preco * quantidade
(5)imposto = se a quantidade for maior que 10 calcule um imposto de 
5% sobre o produto senaõ calcule 10%
(6)valor final = total + imposto
'''
produto=input("Digite seu produto (mouse, teclado ou memoria)").lower()
if (produto=="mouse"):
    preco=10
elif (produto=="teclado"):
    preco=20
elif (produto=="memoria"):
    preco=100
else:
    preco=0
    print("produto nao existe")
qtd=int(input("Digite a quantidade de produtos comprados"))
total=preco*qtd
print(f"o valor da compra será {total}")
if (qtd > 10):
    imposto = total * 0.05 
else:
    imposto = total * 0.10
valorfinal= total + imposto 
print(f"o valor final da compra incluindo impostos será {valorfinal}")
print(f"produto= {produto} , quantidade= {qtd} , imposto= {imposto}")