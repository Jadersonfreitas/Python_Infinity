sexo = str(input("""Escolha uma das opções abaixo:
                 M para Masculino
                 F para feminino 
                 """)).lower().strip()

if len(sexo) ==1:


    match sexo:
        case "m":
            print("voce escolheu o sexo masculino")
        case "f":
            print("voce escolheu o sexo feminino")
        case _:
            print("sexo invalido")

else: 
    print("digite apenas uma letra")
