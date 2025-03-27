from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    #lista = '<ol><li>Gabriel</li><li>O mestre da programação</li><li>Só que não ainda</li></ol>'
    #return HttpResponse(lista)
    return render(
        request,
        'home/index.html'
    )

