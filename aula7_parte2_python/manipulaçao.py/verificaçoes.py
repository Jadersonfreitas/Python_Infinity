def invert(tx):
    return tx [::-1]


def quantidade(tx:str):
    quant = 1
    for letra in tx.strip():
        if letra == " ":
            quant +=1
    return quant        

texto = str(input("digite: "))
print(quantidade(texto))

def palindromo(tx:str):
    texto_sem_espaço = tx.replace(" ","")
    texto_invertido = invert(texto_sem_espaço)
    if texto_sem_espaço == texto_invertido:
        return "É palindromo!"
    else:
        "Não é palindromo!"