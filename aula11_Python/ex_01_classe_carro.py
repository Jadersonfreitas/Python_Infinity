class Carro:
    def __init__(self, marca, modelo, ano, cor, portas, arcondicionado, vidro_eletrico):
        self.ano = ano
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.portas = portas
        self.arcondicionado = arcondicionado
        self.vidro_eletrico = vidro_eletrico


carro1= Carro(marca= "Ford", modelo="Ranger", ano=2023, cor="azul meia noite", portas=4, arcondicionado= True, vidro_eletrico= True)
carro2= Carro(marca= "toyota", modelo= "corolla", ano= 2024, cor= "vermelho 15 pras 6", portas= 4, arcondicionado= True, vidro_eletrico= True)

marca_do_carro = str(input("Digite a marca do seu carro: "))
modelo_do_carro = str(input("Digite o nome do modelo do seu carro: "))
ano_do_carro = int(input("Qual o ano do seu carro: "))
cor_do_carro = str(input("Qual a cor do seu carro: "))
portas_do_carro = int(input("Quantas portas seu carro tem: "))
arcondicionado_do_carro = bool(input("Seu carro tem arcondicionado?: "))
vidro_eletrico_do_carro = bool(input("Seu carro tem vidro_eletrico?: "))

carro3= Carro(marca= marca_do_carro, modelo= modelo_do_carro, ano= ano_do_carro, cor= cor_do_carro, portas= portas_do_carro, arcondicionado= arcondicionado_do_carro, vidro_eletrico= vidro_eletrico_do_carro)    

print(carro1.marca, carro1.modelo)
print(carro2.modelo, carro2.ano)

if carro2.vidro_eletrico:
    print("O segundo carro tem vidro eletrico")
else:
    print("O segundo carro não tem vidro eletrico")

print(f""" 
    Informaçoes do carro 3:
      Marca: {carro3.marca}
      Modelo: {carro3.modelo}
      Ano:    {carro3.ano}
      Cor:    {carro3.cor}
      porta:  {carro3.portas}
      
""")

if carro3.vidro_eletrico:
    print(f"O {carro3.modelo} tem vidro eletrico")
else:
    print(f"O {carro3.modelo} nao tem vidro eletrico")
