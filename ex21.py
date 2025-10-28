"""
Enunciado:
Crie um programa que:
Peça o nome de um aluno e 3 notas.
Calcule a média das notas usando uma função.
Mostre o nome, a média e se ele foi aprovado (≥ 7) ou reprovado (< 7).
"""

def main(nome): # aqui é onde o valor vai ficar armazenado
    return nome # aqui vai retornar

def calcular_nota(n1, n2, n3): # onde fica armazenados
    return (n1 + n2 + n3) / 3 # retorna o resultado

nome_user = input("Digite seu nome: ") # pede o nome 

# pede os numeros
n1 = int(input("Digite a nota 1: "))
n2 = int(input("Digite a nota 2: "))
n3 = int(input("Digite a nota 3: "))

# calcula os numeros
media = calcular_nota(n1, n2, n3)

# retorna com os dados preenchidos e enviados para a funcao
print(f"{main(nome_user)}, sua média é: {media:.2f}")