class Veiculo:
    def __init__(self, marca:str, modelo:str, ano:int, cor:str):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def ligar(self):
        return f"O veiculo {self.modelo} está ligado"
    
    def desligar(self):
        return f"O veiculo {self.modelo} está desligado"



class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, cor: str, qtde_portas:int):
        super().__init__(marca, modelo, ano, cor)
        self.qtde_portas = qtde_portas

    def arcondinionado(self):
        return f"O veiculo {self.modelo} está com o ar-condicionado ligado"


class Moto(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, cor: str, cilindradas:int):
        super().__init__(marca, modelo, ano, cor)        
        self.cilindradas = cilindradas

    def empinar(self):
        return f"A moto {self.modelo} está empinando o pneu"


carro1 = Carro(marca= "Renault", modelo= "Duster", ano= 2015, cor= "braco", qtde_portas= 4)
moto1 = Moto(marca= "Honda", modelo= "pop", ano= 2017, cor= "vermelha", cilindradas= 100)


print(carro1.ligar())
print(moto1.desligar())
print(carro1.arcondinionado())
print(moto1.empinar())
