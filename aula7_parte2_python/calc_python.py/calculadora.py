def soma(x,y):
    return x + y

def sub(x,y):
    return x - y

def vezes(x,y):
    return x * y

def divisao(x,y):
    if y == 0:
        print("erro! não pode dividir por zero")
    else:
        return x / y

def pot(x,y):
    return x ** y

def app(n1,n2):
    while True:
        calculo = str(input(f""" Escolha uma operação matematica:
       
            A - SOMA
            B - SUBTRAÇÂO
            C - MULTIPLICAÇÂO
            D - DIVISÃO
            E - POTÊNCIA
            F - SAIR                

""" )).lower()

        match calculo:
            case "a":
                print(soma(n1, n2))
            case "b":
                print(sub(n1, n2))
            case "c":
                print(vezes(n1, n2))
            case "d":
                print(divisao(n1, n2))
            case "e":
                print(pot(n1, n2))
            case "f":
                print("ATE LOGO")
                break
            case _:
                print("Opção Inválida! ESCOLHA ENTRE A/B/C/D/E/F")