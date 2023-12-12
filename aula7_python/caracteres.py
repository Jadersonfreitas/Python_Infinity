def quant(num):
    return len(num)




def vog(tx):
    cont = 0
    for i in tx:
        if i in "aeiouáàéèìíòóùúôõêã":
            cont += 1
    return cont    
    



def cons(tx):
    cont = 0
    for i in tx:
        if i in "bcdfghjklmnpqrstwxyz":
            cont += 1
    return cont    
    



def vazio(tx):
    cont = 0
    for i in tx:
        if i in " ":
            cont += 1
    return cont    
    
