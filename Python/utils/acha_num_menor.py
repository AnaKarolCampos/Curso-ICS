matriz_numeros = [
    [10, 20, 30, 40, 50],
    [60, 70, 80, 90, 100],
    [110, 120, 130, 140, 150]
]

def acha_menor(lista):

    menor_numero = lista[0]

    for numero in lista:
        if numero < menor_numero:
            menor_numero = numero

    return menor_numero

res = acha_menor(matriz_numeros[-1])
print(res)