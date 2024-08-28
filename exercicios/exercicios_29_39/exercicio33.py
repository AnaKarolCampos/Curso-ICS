nota1 = float(input('Insira a 1° nota: '))
nota2 = float(input('Insira a 2° nota: '))
nota3 = float(input('Insira a 3° nota: '))
nota4 = float(input('Insira a 4° nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print('Aprovado.')

elif 5 <= media < 7:
    print('Em recuperação.')

else:
    print('Reprovado.')