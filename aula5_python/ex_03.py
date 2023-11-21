def custo(valor,hora):
    return valor/hora

while True:
    nome = str(input("Digite o seu nome: "))
    total = float(input("Quanto voce recebeu pelo serviço: "))
    tempo = float(input("quantas horas voce trabalhou: "))

    print(f"voce ganha {custo(total,tempo):.2f} por hora")