def semaforo(tx):
    match tx:
        case  1:
            return "Pode passar!"
        case  2:
            return "ATENÇÃO, JA IRA FECHAR!"
        case 3:
            return "PARE! O SEMAFORO FECHOU!"
        case _:
            return "ERROR! DIGITE UM NUMERO DE 1 A 3"


numero = int(input(f""" 
            Escolha um numero de 1 a 3 para validar o semaforo:
                     1- VERDE
                     2- AMARELO
                     3- VERMELHO

"""))  
print(semaforo(numero))