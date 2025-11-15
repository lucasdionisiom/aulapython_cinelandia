'''Peça dois numeros e uma operação. Use try-except-else-finally para tratar erros como divisão por zero e operação inválida.
Utilize a estrutura match case para decidir com os caracteres abaixo suas respectivas operações: 
+ Adição
- Subtração
* Multiplicação
/ Divisão
'''
def calculadora():
    try:
        a=float(input('Digite o primeiro numero:'))
        b=float(input('Digite o segundo numero:'))
        op=input('Digite a operação (+,-,*,/):')

        match op:
            case '+':
                resultado = a + b
            case '-':
                resultado = a - b
            case '*':
                resultado = a * b
            case '/':
                resultado = a / b 
            case _:
                raise ValueError ("Operação Invalida")
    except ZeroDivisionError:
        print('Erro: divisão por zero')
    except ValueError as e:
        print (f'{e}')
    else:
        print(f'Resultado {resultado}')
    finally:
        print('Calculo encerrado.')

calculadora()