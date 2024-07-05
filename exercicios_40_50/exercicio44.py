lista = [-10, 15, -20, 25, 30]

def retira_nums_negativos(lista):
    positivos = []
    for num in lista:
        if num >= 0:
            positivos.append(num)
    return positivos

resultado = retira_nums_negativos(lista)
print(resultado)