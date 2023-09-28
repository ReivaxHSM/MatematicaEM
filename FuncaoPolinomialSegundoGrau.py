# Programa para calcular Função Polinomial de Segundo Grau
# Autor: Heráclito Santos Martins Xavier
# Data: 21/09/2023
# Versão: 0.0.1

#import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Entrada de dados
print("------------------------------------------------------------")
print("Programa para calcular Função Polinomial de Segundo Grau")
print("------------------------------------------------------------")
a = float(input("Digite o coeficiente a:"))
b = float(input("Digite o coeficiente b:"))
c = float(input("Digite o coeficiente c:"))

# Preencher valores das variáveis indpendentes x1, x2, x3, x4 e x5
print("------------------------------------------------------------")
print("Digite valores aleatórios positivos e/ou negativos para x1, x2, x3, x4 e x5")
x1 = float(input("Digite o valor de x1: "))
x2 = float(input("Digite o valor de x2: "))
x3 = float(input("Digite o valor de x3: "))
x4 = float(input("Digite o valor de x4: "))
x5 = float(input("Digite o valor de x5: "))

# Calcula os valoes de y para x1, x2, x3, x4 e x5
y1 = a*x1**2 + b*x1 + c
y2 = a*x2**2 + b*x2 + c
y3 = a*x3**2 + b*x3 + c
y4 = a*x4**2 + b*x4 + c
y5 = a*x5**2 + b*x5 + c

# Cria a tabela com os valores de x e y
dados = {'Valores de x': [x1,x2,x3,x4,x5], 'Valores de y ou f(x)': [y1,y2,y3,y4,y5]}
tabela = pd.DataFrame(dados)

print("------------------------------------------------------------")
print("************************TABELA****************************** ")
print("------------------------------------------------------------")
print(tabela)

# Cálculo das raízes ou zeros da função
delta = b**2 - 4*a*c
R1 = (-b + np.sqrt(delta))/(2*a)
R2 = (-b - np.sqrt(delta))/(2*a)

print("------------------------------------------------------------")
print(f"A função é y = {a}x² + {b}x + {c}")
print("------------------------------------------------------------")

if delta == 0:
    print("A função possui duas raízes reais e iguais")
    print("A raiz ou zero da função é x = ", R1, " = ", R2  )
    print("------------------------------------------------------------")
    print()

if delta > 0:
    print("A função possui duas raízes reais e distintas")
    print("A primeira raiz ou zero da função é x' = ", R1)
    print("A segunda raiz ou zero da função é x'' = ", R2)
    print("------------------------------------------------------------")

if delta < 0:
    print("A função não possui raízes reais")
    exit()

#Cálculo do vértice da parábola
xv = -b/(2*a)
yV = -delta/(4*a)

print("O vértice da parábola é: (", xv, ",", yV, ")")
print("------------------------------------------------------------")

#Ponto de máximo ou mínimo
if a > 0:
    print("O vértice da parábola é um ponto de mínimo")
    print("------------------------------------------------------------")
else:
    print("O vértice da parábola é um ponto de máximo")
    print("------------------------------------------------------------")

#Conjunto imagem da função
if a > 0:
   print("O conjunto imagem da função é: [", yV, ", +infinito)")
   print("------------------------------------------------------------")
else:
    print("O conjunto imagem da função é: (-infinito, ", yV, "]")
    print("------------------------------------------------------------")

#Plota o gráfico
x = np.arange(-10, 10, 0.1) #Cria um vetor com valores de -10 a 10 com passo de 0.1
y = a*x**2 + b*x + c
plt.title("Função Polinomial de Segundo Grau")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.plot(x, y)
plt.grid(True)
plt.show()
print()

#Fim do programa



