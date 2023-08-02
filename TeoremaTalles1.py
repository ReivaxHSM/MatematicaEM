# Programa específico: Calcular incógnitas do teorema de Tales
# Autor: Heráclito Santos Martins Xavier
# Data: 26/07/2023
# Versão: 0.0.1

# Entrada de Dados
print("Programa para calcular incógnitas do teorema de Tales")
print("---------------------------------------------------")
print("O valor de AB = x + 3")
print("O valor de CD = x - 2")
print("Digite o valor dO segmento MN: ")
MN = float(input())
print("Digite o valor do segmento PQ: ")
PQ = float(input())

# Processamento dos dados
# Cálculo de x
x = (MN * 2 + PQ * 3) / (MN - PQ)

# Cálculo de AB e CD
AB = x + 3
CD = x - 2

# Saída de dados
print(f"AB = {AB} cm")
print(f"CD = {CD} cm")







