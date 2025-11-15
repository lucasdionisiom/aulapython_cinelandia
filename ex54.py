'''Peça dois numeros e uma operação. Use try-except-else-finally para tratar erros como divisão por zero e operação inválida.
Utilize a estrutura match case para decidir com os caracteres abaixo suas respectivas operações: 
+ Adição
- Subtração
* Multiplicação
/ Divisão
'''
def calculadora():
    resultado = None  # Inicializa o resultado
    try:
        # 1. Pedir os números e tentar converter para float (Tratamento de ValueError)
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        # 2. Pedir a operação
        operacao = input("Digite a operação (+, -, *, /): ")
        
        # 3. Decidir a Operação (match case)
        match operacao:
            case '+':
                resultado = num1 + num2
            case '-':
                resultado = num1 - num2
            case '*':
                resultado = num1 * num2
            case '/':
                resultado = num1 / num2
            case _:
                # Gera uma exceção de ValueError se a operação não for reconhecida
                # Isso simula um "Erro de Operação Inválida"
                raise ValueError("Operação Inválida") 

    # 4. Tratar Erros
    except ZeroDivisionError:
        # Captura o erro específico de divisão por zero
        print("❌ Erro: Não é possível dividir por zero.")
    
    except ValueError as e:
        # Captura erros de conversão (letras em vez de números) E "Operação Inválida"
        if "Operação Inválida" in str(e):
            print("❌ Erro: Operação matemática desconhecida. Use apenas +, -, *, /.")
        else:
            print("❌ Erro: Digite apenas números válidos para o cálculo.")


    # 5. Exibir Resultado (Executa SOMENTE se não houver erro no try)
    else:
        # Verifica se o resultado foi realmente calculado (caso tenha passado pelo match)
        if resultado is not None:
            print(f"\n✅ Resultado de {num1} {operacao} {num2}: {resultado:.2f}")
        
    # 6. Finalizar
    finally:
        print("\n=== Fim do programa da Calculadora. ===")

# Chamada da função para iniciar o programa
calculadora()