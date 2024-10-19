from django.contrib import admin
from django.urls import path, include
import exercicios.views
urlpatterns = [
    path('', exercicios.views.home, name='home'),
    path('ex1/', exercicios.views.ex1, name='ex1'),
    path('ex2/', exercicios.views.ex2, name='ex2'),
    path('ex3/', exercicios.views.ex3, name='ex3'),
]