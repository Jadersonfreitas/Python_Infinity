def maior(n1,n2,n3):
    if n1 >= n2 >= n3:
        return f"{n1} É o maior numero!"
    elif n2 >= n1 >= n3:
        return f"{n2} É o maior numero!"
    elif n3 >= n1 >= n2:
        return f"{n3} É o maior numero!"
    
num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
num3 = int(input("Digite o terceiro valor: "))

print(maior(num1,num2,num3))