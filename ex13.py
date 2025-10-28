"""
Enunciado:
Contando até vinte: Use um laço for para exibir os números de 1 a 20, incluindo-os.
"""
# For normal
for n in range(1,21):
    print(n)

# Com List Comprehensions
numbers = [n for n in range(1,21)]
print(numbers)