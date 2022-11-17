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
    return math.log(n, logValue)


# Função Percentagem 
def percentage(n1, n2):
    if n1 > 0 or n2 > 0:
        return str(round((n1 / n2) * 100,2)) + "%"
    else:
        return "Error - Negative numbers"


# Imprime Lista de operações
# Pede número de operação
def printOperation():
    os.system('cls')
    while True:
        try: 
            operation = int(input('''
                Insira a opção matemática que quer calcular:
                    1 - Soma
                    2 - Subtração
                    3 - Multiplicação
                    4 - Divisão
                    5 - Exponencial
                    6 - Percentagem
                    7 - Logarítmica
                    8 - Factorial
                    9 - Raíz Quadrada
                   
                \n\t\tInsira o número da operação: '''))

            
            if operation > 0 and operation <= 9:
                return operation
                break
            else:
                print("\t\tInsira uma operação válida!")
                
        except ValueError:       # Se é causado um erro apresenta ValueError
            os.system('cls')
            print("\t\tInsira uma operação válida!")


# Função que imprime resultado
def printString(string):
    print('\t\tResultado obtido = {}'.format(str(string)))

# Função que pergunta ao utilizador se quer calcular novamente
def again():
    option_again = input('''\n\t\tQuer calcular novamente? \n\t\tS - Sim \n\t\tN - Não \n\t\t> ''')
    os.system('cls')

    if option_again.upper() == 'S':
        main()
    elif option_again.upper() == 'N':
        print('Adeus!')
    else:
        print("\n\t\tOpção Inválida!")
        again()
        

# Função Principal
def main():
    operation = printOperation()

    # Validação para inserir dois valores
    if operation >= 1 and operation <= 7:
        while True:
            try:

                if operation == 6:
                    print('\n\t\tInfo: Primeiro valor corresponde á percentagem a aplicar !')


                n1 = float(input('\t\t> Insira o primeiro número: '))

             
                if operation == 7:
                    print('\n\t\tInfo: Valor do log > 1 e <= 10!')

                    n2 = float(input('\t\t> Insira o segundo número: '))
                    if n2 > 1 and n2 <= 10:
                        break
                    else:
                        print('\n\t\tValor inválido!\n')
                        continue
                
                else:
                    n2 = float(input('\t\t> Insira o segundo número: '))


                if type(n1) == float and type(n2) == float:
                    break

            except ValueError:       # Do this instead if the try block causes a ValueError
                print("\n\t\tInsira um valor válido!")
            
    # Porquê um else? porque na função printOperation() é verificado se o numero está entre 0 e 9 ou igual a 9 
    # Validação insere só um valor, no caso de ser 8 ou 9
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
        printString(percentage(n1, n2))
    
    elif operation == 7:
        printString(log(n1, n2))
    
    elif operation == 8:
        printString(factorial(n2))
        
    # Executa funcao squareRoot (9) pois já foi limitado o valor do número na função printOperation()
    else:
        printString(squareRoot(n2))
        

    # Add again() function to calculate() function
    again()

   
# Execução do código
main()