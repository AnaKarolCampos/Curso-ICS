lista = [5, 3, 9, 1, 10]

def acha_maior(lista):
    maior_numero = lista[0]
    for numero in lista:
        if numero > maior_numero:
            maior_numero = numero
    return maior_numero

resultado = acha_maior(lista)
print(resultado)