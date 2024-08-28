alturas = [165, 170, 180, 175, 160]

def encontra_altura_media(lista):
    soma = 0
    for num in lista:
        soma = soma + num
    media = soma / len(alturas)
    return media

print(f'A altura média é {encontra_altura_media(alturas)}.')