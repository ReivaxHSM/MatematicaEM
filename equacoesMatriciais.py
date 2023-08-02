# Programa para resolver equações matriciais
#-------------------------------------------------------
# Autor: Heráclito Santos Martins Xavier
# Data: 18/07/2023
# Versão: 1.0
#-------------------------------------------------------
# Bibliotecas
#-------------------------------------------------------
import numpy as np
import sympy as sp
import math
import matplotlib.pyplot as plt

#-------------------------------------------------------
# Entrada de dados: número de linhas e colunas das matrizes
#-------------------------------------------------------
print("Programa para resolver equações matriciais")
print("----------------------------------------------------")
print("Digite o número de linhas da matriz A:")
m = int(input())
print("Digite o número de colunas da matriz A:")
n = int(input())
print("Digite o número de linhas da matriz B:")
p = int(input())
print("Digite o número de colunas da matriz B:")
q = int(input())
print()

#-------------------------------------------------------
# Criação das matrizes
#-------------------------------------------------------

A = np.zeros((m,n))
B = np.zeros((p,q))
X = np.zeros((m,q))

#-------------------------------------------------------
# Entrada de dados: elementos das matrizes A e B
#-------------------------------------------------------
print("Digite os elementos da matriz A:")
for i in range(m):
    for j in range(n):
        A[i,j] = float(input())

print("Digite os elementos da matriz B:")
for i in range(p):
    for j in range(q):
        B[i,j] = float(input())
print()

#-------------------------------------------------------
# Processamento da equação matricial
#------------------------------------------------------
X = (B - A)/2
#-------------------------------------------------------
# Saída de dados
#-------------------------------------------------------

print("A matriz A é:")
print(A)
print()
print("A matriz B é:")
print(B)
print()
print("A matriz X é:")
print(X)
print()
print("Fim")
print('----------------------------------------------------')
print()
#-------------------------------------------------------
# Fim
#-------------------------------------------------------



