#Programa para calcular adição e subtração de matrizes
# Autor: Heráclito Santos Martins Xavier
# Data: 18/07/2023
#-------------------------------------------------------

import numpy as np
import sympy as sp
import math
import matplotlib.pyplot as plt

#-------------------------------------------------------
# Entrada de dados
#-------------------------------------------------------
print("Programa para calcular adição e subtração de matrizes")
print("----------------------------------------------------")
print("Digite o número de linhas da matriz A:")
m = int(input()) # Converte o valor digitado para inteiro e armazena em m
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
# Verifica se as matrizes são de mesma ordem para adição e subtração
if m != p or n != q:
    print("As matrizes não são de mesma ordem para adição e subtração")
    print("----------------------------------------------------")
    print("Fim")
    exit()
A = np.zeros((m,n)) # Cria a matriz A preenchida com zeros de dimensões m x n
B = np.zeros((p,q)) # Cria a matriz B preenchida com zeros de dimensões p x q
C = np.zeros((m,n)) 
D = np.zeros((p,q))

#-------------------------------------------------------
# Entrada de dados
#-------------------------------------------------------
print("Digite os elementos da matriz A:")
for i in range(m): # Loop para percorrer todas as linhas da matriz
    for j in range(n): # Loop para percorrer todas as colunas da matriz
        A[i,j] = float(input()) # Solicita ao usuário o valor do elemento da posição (i, j) e o converte para float, armazenando em A[i, j]

print("Digite os elementos da matriz B:")   
for i in range(p):
    for j in range(q):
        B[i,j] = float(input())

#-------------------------------------------------------
# Cálculo da adição e subtração de matrizes
#-------------------------------------------------------
for i in range(m):
    for j in range(n):
        C[i,j] = A[i,j] + B[i,j] # Cálculo da adição de matrizes
        D[i,j] = A[i,j] - B[i,j] # Cálculo da subtração de matrizes

#-------------------------------------------------------
# Saída de dados
#-------------------------------------------------------
print("A matriz A é:")
print(A)
print()
print("A matriz B é:")
print(B)
print()
print("A soma da matriz A + B é:")
print(C)
print()
print("A subtração da matriz A - B é:")
print(D)
print()

#-------------------------------------------------------
# Fim
