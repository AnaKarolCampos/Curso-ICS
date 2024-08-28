palavra = 'ola'

inicio = 0
fim = len(palavra) - 1

palindromo = True

while True:
    if inicio == len(palavra):
        break
    letra_inicio = palavra[inicio]
    letra_fim = palavra[fim]

    if letra_inicio != letra_fim:
        palindromo = False
        break

    inicio = inicio + 1
    fim = fim - 1


if palindromo:
    print('Parabéns! A palavra é um palindromo.')
else:
    print('A palavra não é um palindromo.')