print("**************************  MENU  ******************************\n\n")
print("O que você deseja calcular?\n\n")
print("1 - O enésimo termo de uma Progressão Aritmética\n")
print("2 - A razão de uma Progressão Aritmética\n")
print("3 - O valor da posição n numa Progressão Aritmética\n")
print("4 - A soma dos termos de uma PA\n")
print("5 - O valor de an e da razão a partir da Somda dos termos de uma PA\n")
print("\n*******************************************************************")
print("\n\n")

opcao = int(input())

if opcao == 1:
    a1 = int(input("Digite o 1º termo da PA: "))
    r = int(input("Digite a razão da PA: "))
    n = int(input("Digite o termo da sequência da PA que deseja conhecer: "))

    an = a1 + (n-1)*r

    print(f"O valor do {n}º termo da PA é {an}\n")

elif opcao == 2:
    a1 = int(input("Digite o 1º termo da PA: "))
    an = int(input("Digite o enésimo termo da PA: "))
    n = int(input("Digite o número de termos da PA: "))

    r = (an - a1)/(n - 1)

    print(f"O valor da razão é {r}\n")

elif opcao == 3:
    a1 = int(input("Digite o 1º termo da PA: "))
    an = int(input("Digite o enésimo termo da PA: "))
    r = int(input("Digite a razão da PA: "))

    n = ((an - a1)/(r)) + 1

    print(f"O valor de n corresponde {n} na sequência\n")

elif opcao == 4:
    a1 = int(input("Digite o 1º termo da PA: "))
    r = int(input("Digite a razão da PA: "))
    n = int(input("Digite a posição n da PA: "))

    an = a1 + (n-1)*r
    sn = ((a1 + an)*n)/2

    print(f"O valor da soma dos {n} primeiros números da PA é {sn}\n")

elif opcao == 5:
    a1 = int(input("Digite o 1º termo da PA: "))
    n = int(input("Digite a posição n da PA: "))
    sn = int(input("Digite a soma dos termos da PA: "))

    an = ((2*sn - n*a1))/(n)
    r = (an - a1)/(n - 1)

    print(f"an = {an}\n")
    print(f"razão = {r}\n")

else:
    print("Opção inválida, escolha entre 1 e 5 no menu")