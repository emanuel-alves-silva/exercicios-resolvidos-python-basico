"""
Crie um programa que:

Peça ao usuário uma palavra ou frase.

Use funções pra:

Contar quantas vogais tem.

Contar quantas consoantes tem.

Retorne os dois resultados formatados bonitinho.
"""

texto = input("Digite a palavra: ").lower()

def contar_vogais(palavra):
    vogais = "aeiou"
    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador += 1
    return contador

def contar_consoantes(texto):
    vogais = "aeiou"
    contador = 0
    for letra in texto.lower():
        if letra.isalpha() and letra not in vogais: # isalpha() verifica se é uma letra (a–z, A–Z).
            contador += 1
    return contador

vogais = contar_vogais(texto)
consoantes = contar_consoantes(texto)

print(f"Vogais: {vogais}")
print(f"Consoantes: {consoantes}")