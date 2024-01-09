from tkinter import *

tela = Tk()
tela.title("SOMADOR INICIAL")
tela.geometry("400x400")

def somar():
    num1 = float(entrada1_input.get())
    num2 = float(entrada2_input.get())
    soma = num1 + num2
    resultado.config(text=f"A soma das notas é = {soma}")
    

entrada1_label = Label(tela, text="Digite o primeiro numero: ", bg="black", fg="white", font=("Medieval", 16, "bold", "italic"))
entrada1_label.pack()

entrada1_input = Entry()
entrada1_input.pack()

entrada2_label = Label(tela, text="Digite o segundo numero: ")
entrada2_label.pack()
entrada2_input = Entry()
entrada2_input.pack()

botao1_enviar = Button(tela, text="SOMAR", command = somar)
botao1_enviar.pack()

resultado = Label(text="")
resultado.pack()









tela.mainloop()
