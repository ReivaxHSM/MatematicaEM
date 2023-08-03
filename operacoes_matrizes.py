# Programa para operaçoes com matrizes
# Autor: Heráclito Santos Martins Xavier
# Data: 02/08/2023
# versão 1.0
#-------------------------------------------------------
# Importa a biblioteca NumPy para realizar operações com matrizes
import numpy as np

# Função para imprimir o menu de opções para o usuário
def print_menu():
    print("\nMenu:")
    print("1. Soma de matrizes")
    print("2. Subtração de matrizes")
    print("3. Multiplicação de matrizes")
    print("4. Matriz inversa")
    print("5. Multiplicação de matriz por número real")
    print("6. Determinante de matriz")
    print("7. Sair")

# Função para solicitar ao usuário a entrada de uma matriz
def input_matriz():
    # Pede ao usuário o número de linhas e colunas da matriz
    rows = int(input("Digite o número de linhas da matriz: "))
    cols = int(input("Digite o número de colunas da matriz: "))

    matrix = []  # Lista vazia para armazenar os elementos da matriz
    print("Digite os elementos da matriz (separados por espaço ou nova linha):")
    # Pede ao usuário para digitar os elementos da matriz linha por linha
    for i in range(rows):
        row = list(map(float, input().split()))  # Converte a entrada em uma lista de números float
        matrix.append(row)  # Adiciona a linha à matriz

    return np.array(matrix)  # Retorna a matriz como um array NumPy

# Função para somar duas matrizes
def soma_matrizes():
     
    print("\nDigite a primeira matriz:")
    matrix1 = input_matriz()  # Solicita ao usuário para digitar a primeira matriz
    print("\nDigite a segunda matriz:")
    matrix2 = input_matriz()  # Solicita ao usuário para digitar a segunda matriz
    # A matriz deve ser de mesma ordem para realizar a soma
    if matrix1.shape != matrix2.shape:
        print("As matrizes não são de mesma ordem para adição")
        print("----------------------------------------------------")
        print("Fim")
        exit()
    result = matrix1 + matrix2  # Realiza a soma das matrizes
    print("\nResultado:")
    print(result)

# Função para subtrair duas matrizes
def subtrai_matrizes():
    print("\nDigite a primeira matriz:")
    matrix1 = input_matriz()  # Solicita ao usuário para digitar a primeira matriz
    print("\nDigite a segunda matriz:")
    matrix2 = input_matriz()  # Solicita ao usuário para digitar a segunda matriz
    # A matriz deve ser de mesma ordem para realizar a subtração
    if matrix1.shape != matrix2.shape:
        print("As matrizes não são de mesma ordem para subtração")
        print("----------------------------------------------------")
        print("Fim")
        exit()

    result = matrix1 - matrix2  # Realiza a subtração das matrizes
    print("\nResultado:")
    print(result)
    
# Função para multiplicar duas matrizes
def multiplicacao_matrizes():
    print("\nDigite a primeira matriz:")
    matrix1 = input_matriz()  # Solicita ao usuário para digitar a primeira matriz
    print("\nDigite a segunda matriz:")
    matrix2 = input_matriz()  # Solicita ao usuário para digitar a segunda matriz
    # O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz
    if matrix1.shape[1] != matrix2.shape[0]:
        print("O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz")
        print("----------------------------------------------------")
        print("Fim")
        exit()
    result = np.dot(matrix1, matrix2)  # Realiza a multiplicação das matrizes
    print("\nResultado:")
    print(result)

# Função para encontrar a matriz inversa
def inversa_matriz():
    print("\nDigite a matriz:")
    matrix = input_matriz()  # Solicita ao usuário para digitar a matriz

    try:
        result = np.linalg.inv(matrix)  # Tenta calcular a matriz inversa usando a função inv do NumPy
        print("\nMatriz inversa:")
        print(result)
    except np.linalg.LinAlgError:
        # Se houver um erro, informa ao usuário que a matriz não é inversível
        print("\nNão foi possível encontrar a matriz inversa. A matriz pode não ser inversível.")

# Função para calcular a multiplicação de uma matriz por um escalar
def multiplica_matriz_por_real():
    print("\nDigite a matriz:")
    matrix = input_matriz()  # Solicita ao usuário para digitar a matriz
    scalar = float(input("Digite o escalar: "))  # Solicita ao usuário para digitar o escalar

    result = scalar * matrix  # Realiza a multiplicação da matriz pelo escalar
    print("\nResultado:")
    print(result)

# Função para calcular o determinante de uma matriz
def determinante_matriz():
    print("\nDigite a matriz:")
    matrix = input_matriz()  # Solicita ao usuário para digitar a matriz

    try:
        result = np.linalg.det(matrix)  # Tenta calcular o determinante usando a função det do NumPy
        print("\nDeterminante:")
        print(result)
    except np.linalg.LinAlgError:
        # Se houver um erro, informa ao usuário que a matriz não é inversível
        print("\nNão foi possível encontrar o determinante. A matriz pode não ser inversível.")

# Parte principal do programa
if __name__ == "__main__":# Chama a função para imprimir o menu
    while True:
        print_menu()  # Exibe o menu para o usuário
        opcao = input("Escolha uma opção (1-7): ")  # Solicita ao usuário para escolher uma opção

        if opcao == "1":
            soma_matrizes()  # Chama a função para somar as matrizes
        elif opcao == "2":
            subtrai_matrizes()  # Chama a função para subtrair as matrizes
        elif opcao == "3":
            multiplicacao_matrizes()  # Chama a função para multiplicar as matrizes
        elif opcao == "4":
            inversa_matriz()  # Chama a função para encontrar a matriz inversa
        elif opcao == "5": 
            multiplica_matriz_por_real() # Chama a função para multiplicar a matriz por um escalar
        elif opcao == "6":
            determinante_matriz() # Chama a função para calcular o determinante da matriz
        elif opcao == "7":
            print("Encerrando o programa.")
            break  # Encerra o loop e sai do programa
        else:
            print("Opção inválida. Tente novamente.")