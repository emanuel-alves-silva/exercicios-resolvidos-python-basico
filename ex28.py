"""
    Lê o nome e preço de 'qtd' produtos e retorna:
    - Um dicionário com os produtos e preços
    - O nome do produto mais caro
    - A média dos preços
"""

def cadastrar_produtos(qtd=3):

    produtos = {}

    # loop para cadastrar os produtos
    for i in range(qtd):
        nome = input(f"Digite o nome do produto {i+1}: ")
        preco = float(input(f"Digite o preço do {nome}: R$ "))
        produtos[nome] = preco

    # cálculo do produto mais caro
    mais_caro = max(produtos, key=produtos.get)

    # cálculo da média dos preços
    media = sum(produtos.values()) / len(produtos)

    # retorna tudo
    return produtos, mais_caro, media


# Pega o dados do return em sequencia
produtos, mais_caro, media = cadastrar_produtos()

# Mostrando os valores recebidos
print("\n=== RESULTADOS ===")
print("Dicionário de produtos:", produtos)
print("Produto mais caro:", mais_caro)
print(f"Média dos preços: R$ {media:.2f}")