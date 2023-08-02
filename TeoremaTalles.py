#Programa para calcular incógnitas do teorema de Tales
# Autor: Heráclito Santos Martins Xavier
# Data: 18/07/2023
# Versão: 0.0.1

# Entrada de dados
print("Programa para calcular incógnitas do teorema de Tales")
print("---------------------------------------------------")
print("Digite os valores das incógnitas que deseja calcular")
print("---------------------------------------------------")
print("Digite 0 (zero) para incógnitas que não deseja calcular")
print("---------------------------------------------------")

# Entrada de dados
a = float(input("Digite o valor de a: ")) # Incógnita a
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
d = float(input("Digite o valor de d: "))

# Processamento e saída de dados
if a == 0: # Se a for igual a zero
    a = (b*c)/d # Cálculo de a
    print("O valor de a é: ", a)
elif b == 0: # Se b for igual a zero
    b = (a*d)/c # Cálculo de b
    print("O valor de b é: ", b)
elif c == 0:
    c = (a*d)/b
    print("O valor de c é: ", c)
elif d == 0:
    d = (b*c)/a
    print("O valor de d é: ", d)
else:
    print("Não é possível calcular os valores das incógnitas")
print("-------------------------------------------")
print("Fim do programa")
print()

# Fim do programa








