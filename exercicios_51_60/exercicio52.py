temperaturas = [23, 20, 19, 22, 30, 25]

def maior_temp(lista):
    maior_temp = lista[0]
    for temp in lista:
        if temp > maior_temp:
            maior_temp = temp
    return maior_temp

def menor_temp(lista):
    menor_temp = lista[0]
    for temp in lista:
        if temp < menor_temp:
            menor_temp = temp
    return menor_temp

print(f'A maior temperatura é {maior_temp(temperaturas)} e a menor é {menor_temp(temperaturas)}.')