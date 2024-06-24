dados_usina = [
    ['08:00', 165],
    ['09:00', 195],
    ['10:00', 215],
    ['11:00', 255],
    ['12:00', 275],
]

def acha_horario_mais_produziu(dados_usina):
    maior_atual = dados_usina[0]
    for horario in dados_usina:
        if horario[1] > maior_atual[1]:
            maior_atual = horario
    return maior_atual

def acha_horario_menos_produziu(dados_usina):
    menor_atual = dados_usina[0]
    for horario in dados_usina:
        if horario[1] < menor_atual[1]:
            menor_atual = horario
    return menor_atual

def calcula_total_producao(dados_usina):
    total = 0
    for horario in dados_usina:
        total += horario[1]

    return total

def imprime_relatorio(maior, menor, total):
    print('---------RELATORIO-------------------')
    print(f'A maior producao foi: {maior[1]} que ocorreu no horario: {maior[0]}')
    print(f'A menor producao foi: {menor[1]} que ocorreu no horario: {menor[0]}')
    print(f'A producao total foi: {total} Kw/h')

def relatorio(dados_usina):
    maior_producao = acha_horario_mais_produziu(dados_usina)
    menor_producao = acha_horario_menos_produziu(dados_usina)
    total = calcula_total_producao(dados_usina)
    imprime_relatorio(maior_producao, menor_producao, total)

relatorio(dados_usina)