class Pessoa:
    def __init__(self, nome:str, idade:int, peso:float, genero:str):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.genero = genero

cidadao = Pessoa(nome= "Jaderson", idade= 37, peso= 86, genero= "masculino")    

nome_cidadao = str(input("Digite o nome do cidadao: "))
idade_cidadao = int(input("Digite a idade do cidadao: "))
peso_cidadao = float(input("digite o peso do cidadao: "))
genero_cidadao = str(input("Qual o genero do cidadao: "))


cidadao_de_bem = Pessoa(nome= nome_cidadao, idade= idade_cidadao, peso= peso_cidadao, genero= genero_cidadao)

print(cidadao)
print(cidadao_de_bem)