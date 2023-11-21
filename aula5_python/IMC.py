def imc(peso,altura):
    return (peso/altura)**2

lista = []
pes1 = float(input(f"Digite o peso do 1º atleta: "))
alt1 = float(input(f"Digite a altura do 1º atleta: "))

pes2 = float(input(f"Digite o peso do 2º atleta: "))
alt2 = float(input(f"Digite a altura do 2º atleta: "))

pes3 = float(input(f"Digite o peso do 3º atleta: "))
alt3 = float(input(f"Digite a altura do 3º atleta: "))

pes4 = float(input(f"Digite o peso do 4º atleta: "))
alt4 = float(input(f"Digite a altura do 4º atleta: "))

(lista.append(imc(pes1,alt1)))
(lista.append(imc(pes2,alt2)))
(lista.append(imc(pes3,alt3)))
(lista.append(imc(pes4,alt4)))


print(lista)

    











