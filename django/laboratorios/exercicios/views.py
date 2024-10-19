from django.shortcuts import render

def ex1(request):
    return render (request, 'ex1.html')

def ex2(request):
    data = {}
    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num1')
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