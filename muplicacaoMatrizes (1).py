#Programa para calcular multiplicação de matrizes
# Autor: Heráclito Santos Martins Xavier
# Data: 18/07/2023

# Importação de bibliotecas
import numpy as np

#-------------------------------------------------------
# Entrada de dados
#-------------------------------------------------------
print("Programa para calcular multiplicação de matrizes")
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
# Código para alertar o usuário caso as matrizes não sejam compatíveis
if n != p:
    print("As matrizes não são de mesma ordem para multiplicação")
    print("----------------------------------------------------")
    print("Fim")
    exit()
A = np.zeros((m,n))
B = np.zeros((p,q))
C = np.zeros((m,q))

#-------------------------------------------------------
# Entrada de dados
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
# Cálculo da multiplicação de matrizes
#-------------------------------------------------------
for i in range(m): # linha da matriz A
    for j in range(q): # coluna da matriz B
        for k in range(n): # coluna da matriz A e linha da matriz B
            C[i,j] = C[i,j] + A[i,k]*B[k,j] 

#-------------------------------------------------------
# Saída de dados
#-------------------------------------------------------
print("A matriz A é:")
print(A)
print()
print("A matriz B é:")
print(B)
print()
print("A matriz C é:")
print(C)
print("----------------------------------------------------")
print("Fim")
# Fim


