"""
Enunciado:
O objetivo é descobrir quantas garrafas de uísque duty free você teria que comprar, de modo que a economia em relação ao preço normal nas ruas cobrisse efetivamente o custo das suas férias.

Você receberá o preço de rua principal (normPrice, em £ (libras)), o desconto duty free (desconto, em porcentagem) e o custo das férias (em £).

Por exemplo, se uma garrafa custa £10 normalmente e o desconto duty free é de 10%, você economizaria £1 por garrafa. Se suas férias custarem £500, você terá que comprar 500 garrafas para economizar £500, então a resposta que você devolver deverá ser 500.

Outro exemplo: se uma garrafa custa £12 normalmente e o desconto duty free é de 50%, você economizaria £6 por garrafa. Se suas férias custarem £1000, você terá que comprar 166,66 garrafas para economizar £1000, então sua resposta deve ser 166 garrafas.

Todas as entradas serão números inteiros. Por favor, retorne um número inteiro. Arredondar para baixo.
"""


normPrice = int(input("Digite o preço da garrafa (£): "))
dutyFree = int(input("Digite o desconto (%): "))
costHoliday = int(input("Digite o custo das férias: "))

def calculo(preco_garrafa, desconto, custo_ferias):
    porcentagem = preco_garrafa * (desconto / 100)
    custo = custo_ferias / porcentagem

    return custo

resultado = calculo(normPrice, dutyFree, costHoliday)

print(resultado)