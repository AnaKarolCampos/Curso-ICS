from django.shortcuts import render

def home(request):
    data = {'message':'Olá a partir da view'}
    return render(request, 'home.html', data)