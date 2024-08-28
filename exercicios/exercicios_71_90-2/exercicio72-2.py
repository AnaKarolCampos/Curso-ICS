paises = {
    'Brasil': 'Brasília',
    'EUA': 'Washington',
    'França': 'Paris',
    'Inglaterra': 'Londres',
    'Portugal': 'Lisboa',
}

pais = input('Digite um país:  ')

if pais in paises:
    print(paises[pais])
else:
    print('Tente novamente com outro país.')