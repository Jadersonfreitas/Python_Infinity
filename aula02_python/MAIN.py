produtos = [("Maçã", 2.50), ("Banana", 1.75), ("Laranja", 3.00)]

soma = 0

for item in produtos:
    soma = soma + item[1]

print(f"A soma é: {soma}")