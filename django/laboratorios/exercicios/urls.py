from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ex1/', views.ex1, name='ex1'),
    path('ex2/', views.ex2, name='ex2'),
    path('ex3/', views.ex3, name='ex3'),
    path('ex4/', views.ex4, name='ex4'),
    path('ex5/', views.ex5, name='ex5'),
    path('ex7/', views.ex7, name='ex7'),
    path('ex8/', views.ex8, name='ex8'),
]