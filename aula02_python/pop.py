lista_fruta = ["UVA", "PÊRA", "MELÃO", "MAÇA", "BANANA", "ACEROLA", "ABACAXI"]
frut_out = []
fruta = int(input("""Digite o numero da fruta que voce deseja excluir de acordo com a lista abaixo: 
                  1- UVA
                  2- PERA
                  3- MELAO
                  4- MAÇA
                  5- BANANA
                  6- ACEROLA
                  7- ABACAXI
                """))
match fruta:
    case 1:
        lista_fruta.pop(0)
        print(lista_fruta)
        print(frut_out)
    case 2:
        lista_fruta.pop(1)
    case 3:
        lista_fruta.pop(2)
    case 4:
        lista_fruta.pop(3)
    case 5:
        lista_fruta.pop(4)
    case 6:
        lista_fruta.pop(5)
    case 7:
        lista_fruta.pop(6)
    case _:
        print("Digite apenas entre 1 e 7")

print(lista_fruta)

