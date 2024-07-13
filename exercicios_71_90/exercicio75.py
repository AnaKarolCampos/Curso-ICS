paises = {
    'Brasil': 'Brasília',
    'EUA': 'Washington',
    'França': 'Paris',
    'Inglaterra': 'Londres',
    'México': 'Cidade do México',
    'Espanha': 'Madrid',
    'Irlanda': 'Dublin',
}

for pais, capital in paises.items(): # .items() = itens correspondentes ao dicionário
    print(f'A capital de {pais} é {capital}')