"""
Enunciado:
Ingressos para o cinema: Um cinema cobra preços diferentes para os ingressos de acordo com a idade de uma
pessoa. Se uma pessoa tiver menos de 3 anos de idade, o ingresso será gratuito; se tiver entre 3 e 12 anos, o ingresso
custará 10 dólares; se tiver mais de 12 anos, o ingresso custará 15 dólares. Escreva um laço em que você pergunte a
idade aos usuários e, então, informe-lhes o preço do ingresso do cinema.
"""


while True:

    entrada = input("Digite sua idade (ou 'quit' para encerrar): ")

    if entrada.lower() == 'quit':
        print("Encerrando programa...")
        break

    entrada = int(entrada)

    if entrada < 3:
        print("O ingresso está gratuito!")
    elif entrada >= 3 and entrada <= 12:
        print("O ingresso está custando $10,00!")
    elif entrada > 12:
        print("O ingresso está custando $15,00!")
    else:
        print("Digite a sua idade!")