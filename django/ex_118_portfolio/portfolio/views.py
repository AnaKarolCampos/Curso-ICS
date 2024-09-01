from django.shortcuts import render

def design(request):
    return render(request, 'design.html')

def desenvolvimento(request):
    return render(request, 'desenvolvimento.html')

def completo(request):
    return render(request, 'completo.html')