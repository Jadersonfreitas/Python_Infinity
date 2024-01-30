class Calculadora:
    def __init__(self):
        self.reslutado = 0

    def soma(self, n1:float, n2:float):
        self.reslutado = n1 + n2
        return self.reslutado

    def sub(self, n1:float, n2:float):
        self.reslutado = n1 - n2
        return self.reslutado

    def multi(self, n1:float, n2:float):
        self.reslutado = n1 * n2
        return self.reslutado

    def div(self, n1:float, n2:float):
        if n2 != 0:
            self.resultado = n1 / n2
            return self.resultado
        else:
            return "Error, não é possível dividir por 0"


operacao = Calculadora()

while True:
        
    menu = str(input(f""" Digite qual operação voce deseja executar:
                        1- somar 
                        2- subtrair
                        3- multiplicar
                        4- dividir
                        0- finalizar a calculadora
                        """))
    

    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))


    match menu:
        case 1:
            print(operacao.soma(n1=num1, n2=num2))
        case 2:
            print(operacao.sub(n1=num1, n2=num2))
        case 3:
            print(operacao.multi(n1=num1, n2=num2))
        case 4:
            print(operacao.div(n1=num1, n2=num2))
        case 0:
            break
        case _:
            print("Operação invalida")
