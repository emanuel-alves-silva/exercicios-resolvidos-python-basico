"""
Enunciado:
Nathan adora pedalar. Como Nathan sabe que é importante se manter hidratado, ele bebe 0,5 litro de água por hora de ciclismo. Você recebe o tempo em horas e precisa retornar o número de litros que Nathan beberá, arredondado para baixo.
"""

hour = 0.5

horas_totais = float(input("Digite quantas horas: "))

litros = hour * horas_totais

print(f'Nathan terá que beber {int(litros):.0f} litros de água!')