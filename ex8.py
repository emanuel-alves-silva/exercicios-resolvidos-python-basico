"""
Enunciado:
Tabuada com laço FOR
"""
# FOR normal
numero = int(input("Digite o número da tabuada: ")) # pede um numero ao usuario e transforma em inteiro

print(f"Tabuada do {numero}:")

for i in range(1, 11): # pega numeros de 1 ao 10
    print(f"{numero} x {i} = {numero * i}") # pega o numero da entrada e multiplica pelo numero do range (1 ao 10) e mostra a tabuada

# Com list comprehensions
numero2 = int(input("Digite o número da tabuada: "))

tabuadas = [t for t in range(1, 11)]
for t in tabuadas:
    print(numero2 * t) # pega o numero escolhido e multiplica pelos da lista (1 ao 10)