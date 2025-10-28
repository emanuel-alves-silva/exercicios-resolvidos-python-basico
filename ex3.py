"""
Enunciado:
Escreva um programa que:
-Leia o nome de três produtos e seus respectivos preços.
-Armazene os dados em um dicionário, onde a chave é o nome do produto e o valor é o preço (float).

-Imprima:
-O dicionário completo.
-O produto mais caro.
-A média dos preços.
"""

nome_produto1 = input("Digite o nome do produto 1: ")
preco_produto1 = float(input(f"Digite o preço do {nome_produto1}: R$ "))

nome_produto2 = input("Digite o nome do produto 2: ")
preco_produto2 = float(input(f"Digite o preço do {nome_produto2}: R$ "))

nome_produto3 = input("Digite o nome do produto 3: ")
preco_produto3 = float(input(f"Digite o preço do {nome_produto3}: R$ "))

produtos = {
    nome_produto1: preco_produto1,
    nome_produto2: preco_produto2,
    nome_produto3: preco_produto3
}

mais_caro = max(produtos, key=produtos.get) # max: pega o valor maximo

media = (preco_produto1 + preco_produto2 + preco_produto3) / 3

print(produtos)
print(mais_caro)
print(f"{media:.2f}")