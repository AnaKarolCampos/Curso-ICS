from django.shortcuts import render 

def natureza(request):
    return render(request, 'natureza.html')

def urbanas(request):
    return render(request, 'urbanas.html')