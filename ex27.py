"""
Enunciado:
Nathan adora pedalar. Como Nathan sabe que é importante se manter hidratado, ele bebe 0,5 litro de água por hora de ciclismo. Você recebe o tempo em horas e precisa retornar o número de litros que Nathan beberá, arredondado para baixo.
"""

horas_totais = float(input("Digite quantas horas: "))

def litros_agua(horas_total):
    hour = 0.5
    litros = hour * horas_totais
    return litros

res = litros_agua(horas_totais)
print(f'Nathan terá que beber {int(res):.0f} litros de água!')