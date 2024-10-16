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