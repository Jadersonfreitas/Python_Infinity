from tkinter import *

janela = Tk()
janela.title("aprendendo GRID")
janela.geometry("300x300")


idade_label = Label(text="Digite a sua idade:")
idade_label.grid(row=0, column=0)

idade_input = Entry()
idade_input.grid(row=0, column=1, padx=5, pady=10)

altura_label = Label(text="Digite a sua altura:")
altura_label.grid(row=1, column=0)

altura_input = Entry()
altura_input.grid(row=1,column=1, padx=5, pady=10)

botao = Button(text="Enviar", width=29, pady=10)
botao.grid(row=2, column=0, columnspan= 2)



janela.mainloop()