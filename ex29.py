numero_entrada = int(input("Digite o número: "))

def verificar_numero(num):
    if num % 2:
        print(f"O número {num} é ímpar!")
    else:
        print(f"O número {num} é par!")

verificar_numero(numero_entrada)