# Programa para calcular Função Polinomial de Primeiro Grau
# Autor: Heráclito Santos Martins Xavier
# Data: 18/07/2023
# Versão: 0.0.1

#import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Entrada de dados
print("------------------------------------------------------------")
print("Programa para calcular Função Polinomial de Primeiro Grau")
print("------------------------------------------------------------")
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
x1 = float(input("Digite o valor de x1: "))
x2 = float(input("Digite o valor de x2: "))
x3 = float(input("Digite o valor de x3: "))
x4 = float(input("Digite o valor de x4: "))
x5 = float(input("Digite o valor de x5: "))

# Cálculo da raiz ou zero da função
x = np.arange(-2, 5, 0.1) #Cria um vetor com valores de -2 a 5 com passo de 0.1
y = a*x + b

#Calcula os valores de y para x1, x2, x3, x4 e x5
y1 = a*x1 + b
y2 = a*x2 + b
y3 = a*x3 + b
y4 = a*x4 + b
y5 = a*x5 + b

#Cria a tabela com os valores de x e y
dados = {'Valor de x': [x1,x2,x3,x4,x5], 'Valor de y': [y1,y2,y3,y4,y5]}
tabela = pd.DataFrame(dados)

#Saída de dados
print()
print("------------------------------------------------------------")
print("A função é y = ", a, "x + ", b)
print("------------------------------------------------------------")
print()
print("------------------------------------------------------------")
print("A raiz ou zero da função é: ", -b/a)
print("------------------------------------------------------------")
print()
print(tabela)
print()

# Plotagem do gráfico
plt.title("Função Polinomial de Primeiro Grau")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.plot(x, y)
plt.grid(True)
plt.show()
print()

#Fim do programa


