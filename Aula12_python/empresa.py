class Funcionario:
    def __init__(self, id:int, nome:str, cargo:str, salario:float):
        self.id = id
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

class Empresa:
    def __init__(self):
        self.lista_funcionarios = []
        self.contador = 0
        self.lista_de_removidos = []

    def adicionar(self):
        nome_do_funcionario = str(input("Digite o nome do funcionario: "))
        cargo_do_funcionario = str(input("Digite o cargo do funcionario: "))
        salario_do_funcionario = float(input("Digite o salario do funcionario: "))

        funcionario = Funcionario(nome=nome_do_funcionario, cargo=cargo_do_funcionario, salario=salario_do_funcionario)
        self.lista_funcionarios.append(funcionario)

        self.contador += 1

    
    def excluir(self):
        for funcionario in self.lista_funcionarios:
            print(f"{funcionario.id} - {funcionario.nome} | {funcionario.cargo}")
        
        escolha_excluir = int(input("Digite o numero do funcionarios que voce deseja excluir: "))
        if escolha_excluir >= 0 and escolha_excluir < len(self.lista_funcionarios):
            for funcionario in self.lista_funcionarios:
                if funcionario.id == escolha_excluir:
                    self.lista_de_removidos.append(funcionario)
                    self.lista_funcionarios.remove(funcionario)

    def listar_funciononarios(self):
        for funcionario in self.lista_funcionarios:
            print(f"""
            ID: {funcionario.id}
            Nome: {funcionario.nome}
            Cargo: {funcionario.cargo}
            Salário: {funcionario.salario}
""")

empresa1 = Empresa()

while True:
    menu = int(input("""  
    Escolha uma opçao:
    1- Adicionar Funcionario
    2- Excluir funcionario
    3- Ver todos os funcionarios
    0- SAIR

"""))

    match menu:
        case 1:
            empresa1.adicionar()
        case 2:
            empresa1.exluir()
        case 3:
            empresa1.listar_funciononarios()
        case 0:
            break
        case _:
            print("Opção Inválida")












