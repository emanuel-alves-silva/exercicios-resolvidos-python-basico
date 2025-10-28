"""
Crie um programa que:

Peça ao usuário uma temperatura em graus Celsius.
Use uma função que converta essa temperatura pra Fahrenheit.
Mostre o resultado formatado no final.
Fórmula da conversão: F = (C x 9/5) + 32
"""

user = float(input("Digite a temperatura em °C: ")) # pega o dado

def converte_temp(temperatura): # temperatura vai ser onde o dado vai ser armazenado
    return (temperatura * 9/5) + 32 # depois de armazenado faz o calculo

calculo = converte_temp(user) # pego o dado e jogo na funcao para me retornar o valor 

print(f'A temperatura {user}°C em Fahrenheit é: {calculo:}') # imprimo para visualizar