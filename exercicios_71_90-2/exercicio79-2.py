paises = {
    'Brasil': 'Brasília',
    'EUA': 'Washington',
    'França': 'Paris',
    'Inglaterra': 'Londres',
    'México': 'Cidade do México',
    'Espanha': 'Madrid',
    'Irlanda': 'Dublin',
}

def atualizar_capital(paises, pais, nova_capital):
    if pais in paises:
        paises[pais] = nova_capital
        print(f'A capital de {pais} foi atualizada para {nova_capital}.')
    else:
        print(f'O país {pais} não está no dicionário.')

atualizar_capital(paises, 'Espanha', 'Barcelona')
print(paises)