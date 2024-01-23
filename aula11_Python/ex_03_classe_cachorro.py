class Cachorro:
    def __init__(self, nome:str, raca:str, idade:int):
        self.name = nome
        self.breed = raca
        self.age = idade

    
cao1 = Cachorro(nome="Tirano", raca= "cane corso", idade= 2)

nome_canino = str(input("Digite o nome do cachorro: "))
raca_canino = str(input("Digite a raça do cachorro: "))
idade_canino = int(input("Digite a idade do cachorro: "))

cachorrinho = Cachorro(nome= nome_canino, raca= raca_canino, idade= idade_canino)

print(f"Cachorro: {cao1.name}, da raça: {cao1.breed}, tem {cao1.age} anos de idade")

print(cachorrinho.name, cachorrinho.breed, cachorrinho.age)
        
