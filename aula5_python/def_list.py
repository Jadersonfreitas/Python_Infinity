def maior(lista):
    maior_numero = 0
    for numero in lista:
        if numero > maior_numero:
            maior_numero = numero
    if maior_numero == 0:
        return "Digite numeors positivos"
    else:
        return f"{maior_numero} é o maior numero!"



lista = []
for i in range(1,4):
    numero = int(input(f"Digite o {i}º numero: "))
    lista.append(numero)

    print(lista)

print(maior(lista))