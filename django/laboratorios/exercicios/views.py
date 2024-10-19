from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def ex1(request):
    frase = 'Olá, Mundo!'
    data = {
        'titulo': 'Exercício 1. Olá Mundo',
        'descricao_exercicio': 'Faça um programa que mostre a frase "Olá, Mundo!" ao usuário.',
        'frase': frase
    }
    return render(request, 'ex1.html', data)

def ex2(request):
    subtotal = 100
    taxas = 10
    data = {
        'titulo': 'Exercício 2. Olá Mundo',
        'descricao_exercicio': 'Calculadora.',
        'total': f'a soma do subtotal e taxas é {subtotal + taxas}',
    }
    return render(request, 'ex2.html', data)