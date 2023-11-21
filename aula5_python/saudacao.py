def saudacao(hora):
    if hora >= 5 and hora <= 12:
        return "Bom dia!"
    elif hora >= 13 and hora <= 18:
        return "Boa Tarde!"
    else:
        return "Boa noite!"
    
hr = int(input("digite a hora: "))
print(saudacao(hr))