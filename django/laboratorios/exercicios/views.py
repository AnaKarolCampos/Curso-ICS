from django.shortcuts import render

def home(request):
    return render (request, 'home.html')

def ex1(request):
    return render (request, 'ex1.html')

def ex2(request):
    data = {}
    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        total = int(num1) + int(num2)
        data['total'] = total
    return render (request, 'ex2.html', data)

def ex3(request):
    data = {}
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        frase = f'Seu nome é {nome} e sua idade é {idade}'
        data['frase'] = frase
    return render (request, 'ex3.html', data)

def ex4(request):
    data = {}
    if request.method == 'POST':
        palavra = request.POST.get('palavra')
        qtd = f'{len(palavra)}'
        data['qtd'] = qtd
    return render (request, 'ex4.html', data)

def ex5(request):
    data = {}
    if request.method == 'POST':
        palavra1 = request.POST.get('palavra1')
        palavra2 = request.POST.get('palavra2')
        palavra3 = request.POST.get('palavra3')
        palavra4 = request.POST.get('palavra4')
        palavra5 = request.POST.get('palavra5')
        frase = f'{palavra1} {palavra2} {palavra3} {palavra4} {palavra5}'
        data['frase'] = frase
    return render (request, 'ex5.html', data)

def ex7(request):
    data = {}
    if request.method == 'POST':
        num1 = request.POST.get('num1')
        total = int(num1) + int(num1)
        data['total'] = total
    return render (request, 'ex7.html', data)

def ex8(request):
    data = {}
    if request.method == 'POST':
        num1 = request.POST.get('num1')
        total = int(num1) + 1
        data['total'] = total
    return render (request, 'ex8.html', data)