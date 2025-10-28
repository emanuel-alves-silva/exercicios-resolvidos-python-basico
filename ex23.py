"""
Contagem regressiva
"""

numero_contagem = int(input("Digite o número: "))

def contagem_regressiva(numero):
    while numero >= 0:
        print(numero)
        numero -= 1

contagem_regressiva(numero_contagem)