# Com list comprehensions - tabuada
numero2 = int(input("Digite o número da tabuada: "))

tabuadas = [t for t in range(1, 11)]
for t in tabuadas:
    print(numero2 * t) # pega o numero escolhido e multiplica pelos da lista (1 ao 10)