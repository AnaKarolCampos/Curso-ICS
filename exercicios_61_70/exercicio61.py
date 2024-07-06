numeros_pares = []

def adicionar_nums_pares(lista):
    for num in lista:
        if num % 2 == 0 and num <= 20:
            numeros_pares.append(num)

numeros_a_adicionar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,17, 18, 19, 20, 21, 22, 23, 24]
adicionar_nums_pares(numeros_a_adicionar)
print(numeros_pares)