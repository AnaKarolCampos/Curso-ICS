from django.shortcuts import render

def clientes(request):
    return render(request, 'clientes.html')

def funcionarios(request):
    return render(request, 'funcionarios.html')