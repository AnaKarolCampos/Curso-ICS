from django.shortcuts import render

def eletronicos(request):
    return render(request, 'eletronicos.html')

def moveis(request):
    return render(request, 'moveis.html')

def produtos(request):
    return render(request, 'produtos.html')