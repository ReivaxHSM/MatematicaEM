# Programa para calcular matriz inversa
# ----------------------------------------------------
# Autor: Prof. Heráclito Santos Martins Xavier
# Data: 18/07/2023
# Versão: 1.0
# ----------------------------------------------------
# Biblioteca
# ----------------------------------------------------
import numpy as np

# ----------------------------------------------------
# Entrada de dados: número de linhas e colunas da matriz
# ----------------------------------------------------
print("Programa para calcular matriz inversa")
print("----------------------------------------------------")
print("Digite o número de linhas da matriz:")
m = int(input())
print("Digite o número de colunas da matriz:")
n = int(input())
print()

# ----------------------------------------------------
# Criação das matrizes A e B preenchidas com zeros de dimensões m x n
# ----------------------------------------------------

A = np.zeros((m,n))
B = np.zeros((m,n))

# ----------------------------------------------------
# Entrada de dados: elementos da matriz A
# ----------------------------------------------------
print("Digite os elementos da matriz A:")
# Loop para percorrer todas as linhas da matriz
for i in range(m):
    # Loop para percorrer todas as colunas da matriz
    for j in range(n):
        # Solicita ao usuário o valor do elemento da posição (i, j) e o converte para float, armazenando em A[i, j]
        A[i,j] = float(input())
# Verifica se a matriz A é inversível (tem determinante diferente de zero)
if np.linalg.det(A) == 0:
    print("A matriz A não é inversível")
    print("----------------------------------------------------")
    print("Fim")
    exit()
# ----------------------------------------------------
# Processamento da matriz inversa
# ----------------------------------------------------
# Calcula a matriz inversa de A e armazena em B
B = np.linalg.inv(A)

# ----------------------------------------------------
# Saída de dados
# ----------------------------------------------------
print()
print('----------------------------------------------------')
print("A matriz A é:")
print(A)
print()
print("A matriz inversa de A é:")
print(B)
print()
print("A matriz A*B é:")
print(np.dot(A,B))
print()
print("A matriz B*A é:")
print(np.dot(B,A))
print()
print("A matriz identidade é:")
print(np.dot(A,B))
print()
print("Fim")
print("----------------------------------------------------")
print()

# ----------------------------------------------------
# Fim
# ----------------------------------------------------