
def verific(tx):
    cont = 0
    for i in tx:
        if i in "aeiou":
            cont += 1
    return cont

texto = str(input("digite uma palavra: "))
resposta = verific(texto)

if resposta > 3:
    print(f"{texto} tem {resposta} vogais! É MAIS DE 3 VOGAIS")
else:
    print(f"{texto} tem {resposta} vogais! É MENOS DE 3 VOGAIS")

