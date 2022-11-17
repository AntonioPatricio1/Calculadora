# Importações
import math # Calculos Matemáticos
import os   # Usado Comando ClearScreen

# Função Soma
def sum(n1, n2):
    return n1 + n2

# Função Subtração
def subtract(n1, n2):
    return n1 - n2;

# Função Multiplicação
def multiply(n1, n2):
    return n1 * n2

# Função Divisão
def division(n1, n2):
    return n1 / n2

# Função Factorial
def factorial(n):
    result = 1
    # arredondamento de float, caso seja 3.5, arredonda para 4
    roundedNumber = round(n) 
    
    print('\n\t\tNúmero arredondado para: ', roundedNumber)
    for i in range(1, int(roundedNumber) + 1):
        result = result * i

    return result

# Função Exponencial
def exponential(n1, n2):
    return n1 ** n2

# Função Raíz Quadrada
def squareRoot(n):
    return math.sqrt(n)

# Função Logarítmica
def log(n, logValue):
    return math.log(n, 10)


# Imprime Lista de operações
# Pede número de operação
def printOperation():
    os.system('cls')
    while True:
        try: 
            operation = float(input('''
                Insira a opção matemática que quer calcular:
                    1 - Soma
                    2 - Subtração
                    3 - Multiplicação
                    4 - Divisão
                    5 - Exponencial
                    6 - Logarítmica
                    7 - Factorial
                    8 - Raíz Quadrada
                   
                \n\t\tInsira o número da operação: '''))

            
            if operation > 0 and operation <= 8:
                return operation
                break
                
        except ValueError:       # Se é causado um erro apresenta ValueError
            os.system('cls')
            print("\t\tInsira um valor válido!")

# Função que imprime resultado
def printString(string):
    print('\t\tResultado obtido = {}'.format(str(string)))

# Função que pergunta ao utilizador se quer calcular novamente
def again():
    option_again = input('''\n\t\tQuer calcular novamente? \n\t\tS - Sim \n\t\tN - Não \n\t\t> ''')
    os.system('cls')

    if option_again.upper() == 'S':
        calculate()
    elif option_again.upper() == 'N':
        print('Adeus!')
    else:
        print("\n\t\tOpção Inválida!")
        again()
        

def calculate():
    operation = printOperation()

    # Validação para inserir dois valores
    if operation >= 1 and operation <= 6:
        while True:
            try:
                n1 = float(input('\t\t> Insira o primeiro número: '))

                if operation == 6:
                    print('\n\t\tInfo: Valor do log > 1 e <= 10!')
                    n2 = float(input('\t\t> Insira o segundo número: '))
                    if n2 > 1 and n2 <= 10:
                        break
                    else:
                        print('\n\t\tValor inválido!\n')
                        continue
                
                else:
                    n2 = float(input('\t\t> Insira o segundo número: '))

                if type(n1) == int or float and type(n2) == int or float:
                    break

            except ValueError:       # Do this instead if the try block causes a ValueError
                print("\n\t\tInsira um valor válido!")
            
    # Porquê um else? porque na função printOperation() é verificado se o numero está entre 0 e 8 ou igual a 8 
    # Validação insere um valor, no caso de ser 6, 7 ou 8
    else:
       n2 = float(input('\t\t> Insira um número: '))

    # Validação das operações   
    if operation == 1:
       printString(sum(n1, n2))

    elif operation == 2:
        printString(subtract(n1, n2))

    elif operation == 3:
        printString(multiply(n1, n2))

    elif operation == 4:
        printString(division(n1, n2))

    elif operation == 5:
        printString(exponential(n1, n2))
    
    elif operation == 6:
        printString(log(n1, n2))
    
    elif operation == 7:
        printString(factorial(n2))
        
    # Executa funcao squareRoot (8) pois já foi limitado o valor do número na função printOperation()
    else:
        printString(squareRoot(n2))
        


    # Add again() function to calculate() function
    again()

   
# Execução do código
calculate()