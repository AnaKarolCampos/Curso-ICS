lista = ["maçã", "banana", "cereja"]
elemento = "banana"

def encontra_elemento(lista, elemento):
    for palavra in lista:
        if palavra == elemento:
            return True
    return False
        
resultado = encontra_elemento(lista, elemento)
print(resultado)