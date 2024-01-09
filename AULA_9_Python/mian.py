from tkinter import *

caixinha = Tk()
caixinha.title("aula 1 TK")
caixinha.geometry("300x300")

def saudacao():
    nome = usuario_input.get()
    resultado.config(text=(f"Bem vindo {nome}"))
    


usuario_label = Label(caixinha, text="Digite o nome do usuario")
usuario_label.pack()

usuario_input = Entry()
usuario_input.pack()

botao_enviar = Button(caixinha, text="enviar", command=saudacao)
botao_enviar.pack()

resultado = Label(text="")
resultado.pack()


caixinha.mainloop()