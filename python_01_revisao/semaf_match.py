cor = str(input("""
                Escolhar uma cor do semaforo: 
                1 - Vermelho
                2 - Amarelo
                3 - Verde
                """))

match cor:
    case 1:
        print("pare!")
    case 2:
        print("atenção")
    case 3:
        print("Acelere!")
    case _:
        print("cor inexistente")
        

    