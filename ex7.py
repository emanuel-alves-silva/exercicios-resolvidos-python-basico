"""
Enunciado:
Peça uma palavra e mostre quantas vogais (a, e, i, o, u) ela tem.
(Dica: use um for pra percorrer as letras)
"""
palavra = input("Digite uma palavra: ").lower() # Digitando palavra e transforma tudo em minusculo
vogais = "aeiou" # vogais
contador = 0 # conta o numero de vogais

for letra in palavra: # verifica cada letra da palavra ->
    if letra in vogais: # depois verifica qual é vogal que esta salva na variavel vogais ->
        contador += 1 # conta quantas vogais tem na palavra

print(f"A palavra tem {contador} vogais.")


# Com list comprehension

palavra = input("Digite uma palavra: ").lower() # Digitando palavra e transforma tudo em minusculo
vogais = "aeiou" # vogais
contador = 0 # conta o numero de vogais

verificando_letras = [letra for letra in palavra if letra in vogais]
contador = len(verificando_letras)
print(f"A palavra tem {contador} vogais.")