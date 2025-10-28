"""
Enunciado:
Peça o nome e ano de nascimento e o ano atual e verifique se a pessoa é maior de idade
"""

entrada1 = input("Digite seu nome: ")
entrada2 = int(input("Digite seu ano de nascimento: "))
entrada3 = int(input("Digite o ano atual: "))

calculo = entrada3 - entrada2

if calculo >= 18:
    print(f"{entrada1}, vocẽ é de maior!")
else:
    print(f"{entrada1}, você é de menor!")