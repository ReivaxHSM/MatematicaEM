# Programa para encontrar a função polinomial a partir das coordenadas de dois pontos
# Autor: Heráclito Santos Martins Xavier
# Data: 18/07/2023
# Versão: 0.0.1

import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Entrada de dados
print("------------------------------------------------------------")
print("Programa para encontrar a função polinomial a partir das coordenadas de dois pontos")
print("------------------------------------------------------------")
print("Digite as coordenadas do primeiro ponto")
x1 = float(input("Digite o valor de x1: "))
y1 = float(input("Digite o valor de y1: "))
print("Digite as coordenadas do segundo ponto")
x2 = float(input("Digite o valor de x2: "))
y2 = float(input("Digite o valor de y2: "))
print("------------------------------------------------------------")

# Cálculo da raiz ou zero da função
a = (y2 - y1)/(x2 - x1)
b = y1 - a*x1

# Cria a função y = a*x + b


# Saída de dados
print()
print("------------------------------------------------------------")
print("A função é y = ", a, "x + ", b)
print("------------------------------------------------------------")
print()


