num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
operacao = input('Qual tipo de operação você deseja realizar? Digite "A" para soma, "B" para subtração, "C" para multiplicação e "D" para divisão: ').upper()

if operacao == 'A':
    print(f'A soma entre {num1} e {num2} é {num1 + num2}.')

elif operacao == 'B':
    print(f'A subtração de {num1} por {num2} é {num1 - num2}.')

elif operacao == 'C':
    print(f'A multiplicação entre {num1} e {num2} é {num1 * num2}.')

elif operacao == 'D':
    print(f'A divisão de {num1} por {num2} é {num1 / num2}')

else:
    print("Desculpe, não foi possível realizar tal cálculo. Tente novamente.")