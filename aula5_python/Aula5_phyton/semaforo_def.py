def semaforo(tx):
    if tx == "verde":
        return "Pode passar!"
    elif tx == "amarelo":
        return "Tenha atenção!"
    elif tx == "vermelho":
        return "PARE!!!"
    else:
        return "ERROR! Digite Verde, Amarelo ou Vermelho!"
    
while True:
    cor = str(input(f"""
            Digite uma das 3 cores do semaforo:
            A) Verde
            B) Amarelo
            C) Vermelho

 """)).lower()
    
    resposta = (semaforo(cor))
    if resposta != "ERROR! Digite Verde, Amarelo ou Vermelho!":
        print(resposta)
        break
    else:
        print(resposta)    
