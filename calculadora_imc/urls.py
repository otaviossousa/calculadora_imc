from django.urls import path
from . import views

urlpatterns = [
    path ('', views.calculadora_imc, name='calculadora_imc'),
]