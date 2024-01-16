from tkinter import *

janela  = Tk()
janela.title("Maior numero")
janela.geometry("300x300")

def checar():
    num1 = float(numero1_input.get())
    num2 = float(numero2_input.get())

    if num1 > num2:
        resultado.config(text=f"O {num1} é maior!")
        numero1_input.delete(0, END)
        numero2_input.delete(0, END)
    elif num1 < num2:
        resultado.config(text=f"O {num2} é maior!")
        numero1_input.delete(0, END)
        numero2_input.delete(0, END)
    else:
        resultado.config(text=f"Os numeros são iguais")
        numero1_input.delete(0, END)
        numero2_input.delete(0, END)


numero1_label = Label(text="Digite o primeiro numero").pack()
numero1_input = Entry()
numero1_input.pack()


numero2_label = Label(text="Digite o segundo numero").pack()
numero2_input = Entry()
numero2_input.pack()

botao1 = Button(janela, text="Verificar", command=checar)
botao1.pack()

resultado = Label(text="")
resultado.pack()



janela.mainloop()
