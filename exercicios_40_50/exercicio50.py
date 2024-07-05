lista = [1, 2, 3, 4, 5]

def reverte_lista(lista):
    x = len(lista) -1
    lista_aux = []
    while x >= 0:
        num = lista[x]
        lista_aux.append(num)
        x = x -1
    return lista_aux

lista_revertida = reverte_lista(lista)
print(lista_revertida)