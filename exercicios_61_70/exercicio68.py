lista_elementos = [1, 2, 3, 4]

def triplicar_elementos(lista):
    nova_lista = []
    for elemento in lista:
        nova_lista.extend([elemento] * 3)
    return nova_lista

resultado = triplicar_elementos(lista_elementos)
print(resultado)