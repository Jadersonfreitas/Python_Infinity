nome = str(input("Digite o nome do aluno: "))
sobrenome = str(input("Digite o sobrenome: "))
idade = int(input("Digite a idade: "))
email = str(input("Digite o email: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))



aluno = {
"nome": nome, 
"sobrenome": sobrenome, 
"idade": idade,
"email": email,
"nota": [nota1, nota2, nota3, nota4] 
 
}

print(aluno)