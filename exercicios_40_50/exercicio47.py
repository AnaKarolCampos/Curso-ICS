lista = [1, 2, 3, 4, 5]

def filtrar_impares(lista):
    impares_ao_quadrado = []
    for num in lista:
        if num % 2 == 1:
            num = num ** 2
            impares_ao_quadrado.append(num)
    return impares_ao_quadrado

resultado = filtrar_impares(lista)
print(resultado)