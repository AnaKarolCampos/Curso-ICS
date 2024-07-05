lista = [1, 4, 7, 3]

def somar(lista):
    total = 0
    for num in lista:
        total += num
    return total
    
print(somar(lista))