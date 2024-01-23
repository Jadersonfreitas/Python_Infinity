class Celular:
    def __init__(self, marca, modelo, cor, ano, armazenamento):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.armazenamento = armazenamento

celular1 = Celular(marca="samsumg", modelo="s20fe", cor="carambola", ano=2022, armazenamento=1024)
celuar2 = Celular("samsumg", "s20fe", "carambola", 2022, 1024)
celular3 = Celular(modelo="s20fe", cor="carambola", marca= "samsumg", armazenamento=1024, ano=2022)


print(celular1.marca, celular1.modelo)