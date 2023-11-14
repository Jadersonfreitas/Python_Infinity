nome = str(input("Digite o nome do aluno: ")).lower()

while True:
  
    n1 = float(input("Insira a primeira nota: "))
    if n1 >= 0 and n1 <= 10:
        print("nota valida")
        break
    else: 
        print("digite um numero entre 0 e 10")
    
while True:
    n2 = float(input("Insira a segunda nota: "))
    if n2 >= 0 and n2 <= 10:
        print("nota valida")
        break
    else: 
        print("digite um numero entre 0 e 10")
    
while True:
    n3 = float(input("Insira a terceira nota: "))    
    if n3 >= 0 and n3 <= 10:
       print("nota valida")
       break
    else: 
        print("digite um numero entre 0 e 10")
    
while True:
    n4 = float(input("Insira a quarta nota: "))   
    if n4 >= 0 and n4 <= 10:
        print("nota valida")
        break
    else: 
        print("digite um numero entre 0 e 10")

media = (n1 + n2 + n3 + n4)/4    

if n1 >= n2 and n1 >= n3 and n1 >= n4:
    n1 = maior
elif n2 >= n1 and n2 >= n3 and n2 >= n4:
    n2 = maior
elif n3 >= n1 and n3 >= n2 and n3 >= n4:
    n3 = maior
else:
    n4 = maior

aluno = {
    "aluno": nome,
    "notas": [n1, n2, n3, n4],
    "media": media,
    "maior": maior,
    "menor": menor,
}
print(aluno)

