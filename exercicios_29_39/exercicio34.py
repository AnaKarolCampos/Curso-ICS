num = 7
palpite = int(input('Ecolha um número aleatório entre 1 e 10: '))

if palpite == num:
    print('Parabéns! Você acertou.')

elif palpite < num:
    print('Poxa! O seu palpite foi menor que o número certo.')

else:
    print('Poxa! O seu palpite foi maior que o número certo.')