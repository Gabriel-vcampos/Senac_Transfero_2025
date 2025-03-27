from django.http import HttpResponse
from django.shortcuts import render


def contato(request):
    pagina = '<body bgcolor= "#FFF8DC"><h1>Python</h1><p>gabrielprogramador@gmail.com</p></body>'
    return HttpResponse(pagina)
# Create your views here.
