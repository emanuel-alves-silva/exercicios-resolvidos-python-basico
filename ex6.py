"""
Enunciado:
Peça ao usuário 5 produtos (usando um for) e salve numa lista.
Depois mostre todos os produtos digitados.
"""

lista_produtos = []

for i in range(5):
    entradas = input('digite o nome do produto: ')
    lista_produtos.append(entradas)
print(lista_produtos)