entrada1 = input("Digite seu nome: ")
entrada2 = int(input("Digite seu ano de nascimento: "))
entrada3 = int(input("Digite o ano atual: "))

def verificar_idade(nome, data_nascimento, ano_atual):
    calculo = ano_atual - data_nascimento
    if calculo >= 18:
        print(f"{nome}, vocẽ é de maior!")
    else:
        print(f"{nome}, você é de menor!")

res = verificar_idade(entrada1, entrada2, entrada3)