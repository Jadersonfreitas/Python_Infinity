frutas = ["UVA", "PÊRA", "MELÃO", "MAÇA", "BANANA", "ACEROLA", "ABACAXI"]
while True:
    print(frutas)
    menu = int(input(""" 
                     Escolha uma opção:
      1- Excluir a ultima fruta
      2- Escolha qual fruta excluir
      0- sair
                      """))
    match menu:
        case 1:
            frutas.pop()
        case 2:
            print(frutas)
            posicao = int(input("Escolha a posição da fruta que voce quer apagar: "))
            frutas.pop(posicao-1)
        case 0:
            print("FIM")
            break
        
        case _:
            print("Opção invalida")

