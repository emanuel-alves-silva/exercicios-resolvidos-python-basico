"""
Retornando maior numero da lista
"""

numero1 = int(input("Digite: "))
numero2 = int(input("Digite: "))
numero3 = int(input("Digite: "))
numero4 = int(input("Digite: "))

def retorna_numero(*lista):
    lista = list(lista)
    numero = max(lista)
    return numero

resultado = retorna_numero(numero1, numero2, numero3, numero4)
print(resultado)