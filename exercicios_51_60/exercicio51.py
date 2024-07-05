numeros_impares = []

def adicionar_nums_impares(lista):
    for num in lista:
        if num % 2 == 1 and num <= 15:
            numeros_impares.append(num)

numeros_a_adicionar = [1, 3, 4, 7, 10, 15, 16, 17]
adicionar_nums_impares(numeros_a_adicionar)
print(numeros_impares)