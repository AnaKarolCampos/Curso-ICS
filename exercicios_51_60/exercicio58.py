lista_original = [1, 2, 3, 4]

def duplicar_elementos(lista):
    nova_lista = []
    for elemento in lista:
        nova_lista.append(elemento)
        nova_lista.append(elemento)
    return nova_lista

resultado = duplicar_elementos(lista_original)
print(resultado)