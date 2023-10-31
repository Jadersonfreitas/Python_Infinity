cor = str(input("Escolha a cor do semaforo: ")).lower()

if cor == "vermelho":
    print("pare!")
elif cor == "amarelo":
    print("atenção!")
elif cor =="verde":
    print("pode avançar!")
else:
    print("cor inexistente no semaforo!")
