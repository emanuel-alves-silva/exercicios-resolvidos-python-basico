# Verificando vogais com list comprehension

palavra = input("Digite uma palavra: ").lower() # Digitando palavra e transforma tudo em minusculo
vogais = "aeiou" # vogais
contador = 0 # conta o numero de vogais

verificando_letras = [letra for letra in palavra if letra in vogais]
contador = len(verificando_letras)
print(f"A palavra tem {contador} vogais.")