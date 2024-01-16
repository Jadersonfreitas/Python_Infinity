from tkinter import *

janela = Tk()
janela.title("Aprendendo Place")
janela.geometry("300x300")

idade_label = Label(text="Digite a sua idade:")
idade_label.place(x=5, y=5)

idade_input = Entry()
idade_input.place(x=110, y=5)

altura_label = Label(text="Digite a sua altura")
altura_label.place(x=5, y=30)

altura_input = Entry()
altura_input.place(x=110, y=30)
janela.mainloop()