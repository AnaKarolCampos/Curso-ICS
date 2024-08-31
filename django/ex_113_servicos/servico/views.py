from django.shortcuts import render

def web(request):
    return render(request, 'web.html')

def marketing(request):
    return render(request, 'marketing.html')

def todos_servicos(request):
    return render(request, 'todos_servicos.html')