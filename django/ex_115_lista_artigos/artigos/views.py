from django.shortcuts import render

def tecnologia(request):
    return render(request, 'tecnologia.html')

def saude(request):
    return render(request, 'saude.html')

def todos_artigos(request):
    return render(request, 'todos_artigos.html')