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
        'titulo': 'Exercício 2. Calculadora',
        'descricao_exercicio': 'Calculadora.',
        'total': f'a soma do subtotal e taxas é {subtotal + taxas}',
    }
    return render(request, 'ex2.html', data)

def ex3(request):
    data = {
        'titulo': 'Exercício 3. Calculo de total',
        'descricao_exercicio': 'Pedir ao usuário para inserir dois números e então faz a soma deles.',
    }  
    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        total = int(num1) + int(num2)

        data['total'] = total
        
    return render(request, 'ex3.html', data)