"""
Enunciado:
Ingredientes para uma pizza: Escreva um laço que peça ao usuário para fornecer uma série de ingredientes
para uma pizza até que o valor 'quit' seja fornecido. À medida que cada ingrediente é especificado, apresente uma
mensagem informando que você acrescentará esse ingrediente à pizza.
"""

lista = []

while True:
    ingredientes = input("Digite o nome do ingrediente ou 'quit' para sair do programa: ")
    if ingredientes.lower() == 'quit':
        print("Encerrando programa...")
        break
    else:
        print(f'{ingredientes} será adicionado á lista de ingredientes!')
        lista.append(ingredientes)
        print(lista)