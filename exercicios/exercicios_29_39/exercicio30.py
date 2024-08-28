num1 = float(input('Insira um número: '))
num2 = float(input('Insira outro número: '))

if num1 > num2:
    print(f'{num1} é maior que {num2}.')

elif num1 < num2:
    print(f'{num2} é maior que {num1}.')

else:
    print('Os dois números são iguais.')