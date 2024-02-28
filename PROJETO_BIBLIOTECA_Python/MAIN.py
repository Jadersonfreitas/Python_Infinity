# id_livro = 1
# numero_membro = 1

# class Livro:
#     def __init__(self, id:int, titulo:str, autor:str) -> None:
#         self.id = id
#         self.titulo = titulo
#         self.autor = autor
#         self.disponivel = True


# class Membro:
#     def __init__(self, numero:int, nome:str) -> None:
#         self.numero = numero
#         self.nome = nome
#         self.historico = []

# class Biblioteca:
#     def __init__(self) -> None:
#         self.catalogo_livros = []
#         self.registro_membros = []

#     def adicionar_livro(self):
#         global id_livro

#         titulo_livro = str(input("Digite o título do livro: "))
#         autor_livro = str(input("Digite o autor do livro: "))

#         livro_criado = Livro(id=id_livro, titulo=titulo_livro, autor=autor_livro)
        
#         id_livro += 1

#         self.catalogo_livros.append(livro_criado)

#     def adicionar_membro(self):
#         global numero_membro

#         nome_membro = str(input("Digite o nome do membro: "))

#         membro_criado = Membro(numero=numero_membro, nome=nome_membro)
        
#         numero_membro += 1

#         self.registro_membros.append(membro_criado)

#     def emprestar_livro(self):
#         while True:
#             try:
#                 id_membro_escolhido = int(input("Digite o ID do Membro que vai pegar o livro emprestado: "))
#                 break
#             except:
#                 print("Digite apenas o numero do ID")
#         for membro_atual in self.registro_membros:
#             if membro_atual.id == id_membro_escolhido:
#                 while True:
#                     try:
#                         id_livro_escolhido = int(input("Digite o ID do livro que o membro quer emprestado: "))
#                         break
#                     except:
#                         print("Digite apenas o numero do ID")
#                 for livro_atual in self.catalogo_livros:
#                     if livro_atual.id == id_livro_escolhido and livro_atual.disponivel:
#                         livro_atual.disponivel = False
#                         membro_atual.historico.append(livro_atual)
#                         return f"Livro {livro_atual.titulo} foi alugado para o {membro_atual.nome}!"


#     def devolver_livro(self):
#         while True:
#             try:
#                 id_livro_escolhido = int(input("Digite o ID do livro a ser devolvido: "))
#                 break
#             except:
#                 print("Digite apenas o numero do ID")
#         for livro_atual in self.catalogo_livros:
#             if livro_atual.id == id_livro_escolhido and livro_atual.disponivel == False:
#                 livro_atual.disponivel == True
#                 return f"Livro {livro_atual.titulo} foi devolvido!"
           

#     def pesquisar_livro(self):
#         termo_pesquisado = str(input("""
#         Digite uma das opções 
#         Título do livro
#         ID do livro
#         Autor do livro """))

#         nao_tem_no_catalogo = True

#         for livro_atual in self.catalogo_livros:
#             if livro_atual.titulo == termo_pesquisado or livro_atual.autor == termo_pesquisado or str(livro_atual.id) == termo_pesquisado:
#                 nao_tem_no_catalogo = False
#                 print(f"""
#                 Informações do Livro Encontrado:
#                 ID do Livro: {livro_atual.id} 
#                 Título do Livro: {livro_atual.titulo} 
#                 Autor do Livro: {livro_atual.autor} 
#                 Status de disponibilidade do Livro: {livro_atual.disponivel} """)
        
#         if nao_tem_no_catalogo:
#             print("Livro não encontrado")

# biblioteca_atual = Biblioteca()

# while True:
#     menu = int(input("""
#     Escolha uma opção
#     1 - Adicionar Livro
#     2 - Adicionar Membro
#     3 - Emprestar Livro
#     4 - Devolver Livro
#     5 - Pesquisar Livro
#     0 - Sair
# """))
#     match menu:
#         case 1:
#             print(biblioteca_atual.adicionar_livro())
#         case 2:
#             print(biblioteca_atual.adicionar_membro())
#         case 3:
#             print(biblioteca_atual.emprestar_livro())
#         case 4:
#             print(biblioteca_atual.devolver_livro())
#         case 5:
#             biblioteca_atual.pesquisar_livro()
#         case 0:
#             break
#         case _:
#             print("Opção Inválida")
