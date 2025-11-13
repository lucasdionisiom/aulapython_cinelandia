'''Função

Uma função em um algoritmo é um bloco de código nomeado que
realiza uma tarefa específica e retorna um valor após sua execução.
Elas servem para modularizar o programa, reutilizar código e torná-lo
mais legível, evitando repetição. A principal diferença entre uma
função e um procedimento é que a função obrigatoriamente usa o
comando retorne para devolver um resultado, enquanto um
procedimento não retorna valor, mas pode modificar variáveis.

Características principais de uma função:
Retorno de valor: A função retorna um valor para quem a chamou, que
pode ser usado em expressões ou atribuído a uma variável.
Obrigação de retornar: O uso do comando retorne é obrigatório para
indicar qual valor a função devolverá ao programa principal.
Parâmetros: Uma função pode aceitar parâmetros, que são valores de
entrada para processamento interno.
Reutilização de código: Permite que um mesmo trecho de código seja
executado várias vezes sem a necessidade de reescrevê-lo.
Modularização: Divide o programa em partes lógicas menores e mais
fáceis de entender.
Escopo local: Variáveis declaradas dentro da função têm escopo local, o
que significa que só existem e são acessíveis dentro do bloco da função

Uma função em Python é um bloco de código reutilizável que executa uma tarefa específica.
Elas são definidas usando a palavra-chave def, seguidas por um nome, parênteses e dois
pontos. Funções podem receber dados (parâmetros), processá-los e retornar um resultado
usando a palavra-chave return. Elas ajudam a organizar o código, torná-lo mais legível e a
evitar repetições.
ex 1
'''

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def mult(a, b):
    return a * b

def divi(a, b):
    if b != 0:
       a / b
    else:
       print("valor inválido")

num1= int(input("Digite o primeiro número"))
num2= int(input("Digite o primeiro número"))
x=divi(num1, num2)

print(f"Resultado da operação: {x}")
