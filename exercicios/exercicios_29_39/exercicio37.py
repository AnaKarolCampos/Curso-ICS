anos_bissextos = [1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052]
ano = int(input('Digite um ano entre 1988 e 2052 para saber se é bissexto: '))

if ano in anos_bissextos:
    print(ano, 'é bissexto.')

else:
    print(ano, 'não é bissexto.')