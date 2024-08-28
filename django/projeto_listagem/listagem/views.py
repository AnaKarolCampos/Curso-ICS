from django.shortcuts import render

def eletronicos(request):
    dados = {
        'produtos_eletronicos': [
            'Smartphone',
            'Laptop',
            'Tablet',
            'Televisão',
            'Fone de ouvido',
            'Câmera digital',
            'Smartwatch',
            'Console de videogame',
            'Carregador portátil (Power Bank)',
            'Caixa de som Bluetooth'
]
    }
    return render(request, 'eletronicos.html')

def moveis(request):
    return render(request, 'moveis.html')

def produtos(request):
    return render(request, 'produtos.html')