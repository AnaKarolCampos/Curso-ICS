lista = ["maçã", "banana", "kiwi", "abacate", "uva"]

def conta_caracteres(lista):
    x = 0
    while x <= 4:
        for palavra in lista:
            if len(palavra) >= 4:
                print(lista[x])
            x = x + 1
        return

resultado = conta_caracteres(lista)
print(resultado)