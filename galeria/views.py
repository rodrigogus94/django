from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>SuporTI</h1><p> Bem vindo ao space <p>')