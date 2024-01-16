from tkinter import *

janela  = Tk()
janela.title("Hora Trabalhada")
janela.geometry("400x150")


def verificar():
    num1 = float(salario_input.get())
    num2 = float(hora_input.get())
    valor = num1/num2

    if valor >= 0 and valor <= 10:
        resultado.config(text=f"Voce recebe: R${valor:.2f} reais por hora trabalhada", fg="red")
        salario_input.delete(0, END)
        hora_input.delete(0, END)
    elif valor >= 11 and valor <= 25:
        resultado.config(text=f"Voce recebe: R${valor:.2f} reais por hora trabalhada", fg="orange")
        salario_input.delete(0, END)
        hora_input.delete(0, END)
    elif valor >= 26 and valor <= 50:
        resultado.config(text=f"Voce recebe: R${valor:.2f} reais por hora trabalhada", fg="blue")
        salario_input.delete(0, END)
        hora_input.delete(0, END)
    elif valor > 51:
        resultado.config(text=f"Voce recebe: R${valor:.2f} reais por hora trabalhada", bg="black", fg="pink")
        salario_input.delete(0, END)
        hora_input.delete(0, END)
    else:
        resultado.config(text=f"O valor {valor:.2f} é menor que zero!!! Voce esta num trabalho escravo!", fg="purple")
        salario_input.delete(0, END)
        hora_input.delete(0, END)

    
        

salario_label = Label(text="Insira quanto voce ganha por mês:")
salario_label.place(x=10, y=10)
salario_input = Entry()
salario_input.place(x=250,y=10)


hora_label = Label(text="Insira Quantas horas voce trabalha por mês:")
hora_label.place(x=10, y=30)
hora_input = Entry()
hora_input.place(x=250,y=30)

botao1 = Button(janela, text="Calcular", command=verificar)
botao1.place(x=30,y=50)

resultado = Label(text="")
resultado.place(x=100,y=100)



janela.mainloop()

