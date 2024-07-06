nums = [1, 2, 3, 4, 5]

def encontra_produto(lista):
    multip = 1
    for num in lista:
        multip *= num
    return multip

print(encontra_produto(nums))