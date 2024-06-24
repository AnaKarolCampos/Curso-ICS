lista = [1, 2, 3, 4, 5]

def multiplica(lista):
    nova_lista = []
    for numero in lista:
        resultado = numero * numero
        nova_lista.append(resultado)
    return nova_lista