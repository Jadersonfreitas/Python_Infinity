from tkinter import *

janela  = Tk()
janela.title("Hora Trabalhada")
janela.geometry("400x400")

def checar_cor(cor):
    if cor == "vermelho":
        resultado.configure(text="Pare!")
    elif cor == "amarelo":
        resultado.configure(text="Atenção!")
    elif cor == "verde":
        resultado.configure(text="Prossiga!")
   
       

bt_vermelho = Button(bg="red", width=20, height=4, command=lambda : checar_cor("vermelho"))
bt_vermelho.pack()

bt_amarelo = Button(bg="yellow", width=20, height=4, command=lambda : checar_cor("amarelo"))
bt_amarelo.pack()

bt_verde = Button(bg="green", width=20, height=4, command=lambda : checar_cor("verde"))
bt_verde.pack()

resultado = Label(text="")
resultado.pack()


janela.mainloop()

