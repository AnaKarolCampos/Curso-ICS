lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def filtrar_pares(lista):
    pares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
    return pares

pares = filtrar_pares(lista)
print(pares)