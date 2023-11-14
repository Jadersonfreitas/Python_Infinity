nome = str(input("Digite seu nome: "))
sobrenome = str(input("Digite seu sobrenome: "))
idade = int(input("Digite seu idade: "))
email = str(input("Digite seu email: "))

dados_pessoais = {
    "Nome": nome,
    "Sobrenome": sobrenome,
    "Idade": idade,
    "Email": email,
}

print(f"""
      1 - {dados_pessoais['Nome']}
      2 - {dados_pessoais['Sobrenome']}
      3 - {dados_pessoais['Idade']}
      4 - {dados_pessoais['Email']}
""")

lista_de_notas = []
maior_nota = 0
menor_nota = float("inf")
soma = 0
aprovado = "Reprovado"

for i in range(1,5):
    nota = float(input(f"Digite a {i}º nota: "))

    lista_de_notas.append(nota)

    soma += nota

    if nota > maior_nota:
        maior_nota = nota

    if nota < menor_nota:
        menor_nota = nota

media = soma / len(lista_de_notas)

if media >= 7:
    aprovado = "Aprovado"

dados_escola = {
    "Notas": lista_de_notas,
    "Maior_nota": maior_nota,
    "Menor_nota": menor_nota,
    "Média": media,
    "Situação": aprovado
}

dados_pessoais.update(dados_escola)

print(dados_pessoais)

