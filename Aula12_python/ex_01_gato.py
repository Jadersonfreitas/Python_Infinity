class Gato:
    def __init__(self, nome:str, idade:int, peso:float, cor:str, raca:str):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.cor = cor
        self.raca = raca

    def miar(self):
        return f"O gato {self.nome} está miando"
                
    def comer(self):
        return f"O gato {self.nome} está comendo"
    
    def info(self):
        return f""" 
        Nome: {self.nome}
        Idade do gato: {self.idade} anos
        Peso do gato: {self.peso} kilos
        Cor do gato: {self.cor}
        Raça do gato: {self.raca}
"""


nome_do_gato = str(input("Digite o nome do gato: "))
idade_do_gato = int(input("Digite a idade do gato: "))
peso_do_gato = float(input("Digite o peso do gato: "))
cor_do_gato = str(input("Digite a cor do gato: "))
raca_do_gato = str(input("Digite a raça do gato: "))



gato1 = Gato(nome= nome_do_gato, idade= idade_do_gato, peso= peso_do_gato, cor= cor_do_gato, raca= raca_do_gato)

nome_do_gato = str(input("Digite o nome do segundo gato: "))
idade_do_gato = int(input("Digite a idade do segundo gato: "))
peso_do_gato = float(input("Digite o peso do segundo gato: "))
cor_do_gato = str(input("Digite a cor do segundo gato: "))
raca_do_gato = str(input("Digite a raça do segundo gato: "))


gato2 = Gato(nome= nome_do_gato, idade= idade_do_gato, peso= peso_do_gato, cor= cor_do_gato, raca= raca_do_gato)

print(gato1.miar())
print(gato1.comer())
print(gato1.info())


print(gato2.miar())
print(gato2.comer())
print(gato2.info())