from django.shortcuts import render

def futuros(request):
    return render(request, 'futuros.html')

def passados(request):
    return render(request, 'passados.html')

def todos_eventos(request):
    return render(request, 'todos.html')