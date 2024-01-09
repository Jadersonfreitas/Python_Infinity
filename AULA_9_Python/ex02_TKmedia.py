from tkinter import *

tela = Tk()
tela.title("Calculo de media")
tela.geometry("400x400")
tela.config(bg="#131466")


def somar():
    nota1 = float(valor1_input.get())
    nota2 = float(valor2_input.get())
    nota3 = float(valor3_input.get())
    media = (nota1 + nota2 + nota3)/3
    if media >=7 and media < 10:
        resultado.config(text=f"""Sua media foi {media:.2f} 
            Você foi aprovado!""", bg="#276a1d", fg="#e2e2e2")
    elif media < 7:
        resultado.config(text=f"""Sua media foi {media:.2f} 
            voce foi reprovado!""", bg="#b00800", fg="#e2e2e2")
    elif media == 10:
        resultado.config(text=f"""Sua media foi {media:.2f} 
            Voce foi aprovado com distinção!""", bg="#0a5c9a", fg="#e2e2e2")
    else:
        resultado.config(text=f"A media {media} é invalida! Digite apenas notas de 1 a 10", bg="#f9ff4f", fg="#311303")

    
    

valor1_label = Label(text="Digite a primeira nota:")
valor1_label.pack()
valor1_input = Entry()
valor1_input.pack()



valor2_label = Label(text="Digite a segunda nota:")
valor2_label.pack()
valor2_input = Entry()
valor2_input.pack()



valor3_label = Label(text="Digite a terceira nota:")
valor3_label.pack()
valor3_input = Entry()
valor3_input.pack()



botao_soma = Button(tela, text="Tire a média", command= somar)
botao_soma.pack()

resultado = Label(text="", bg="#131466", fg="#e2e2e2")
resultado.pack()

















tela.mainloop()
