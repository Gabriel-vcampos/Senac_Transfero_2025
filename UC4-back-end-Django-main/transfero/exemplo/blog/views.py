from django.http import HttpResponse
from django.shortcuts import render


def blog(request):
   # print('Passei pelo blog maluco')
   # return HttpResponse('<body bgcolor="red"><h1>Alô mundo!</h1></body>')
        # Create your views here.
    return render(
        request, 
        'blog/index.html'
        )

def artigo(request):
    return render(
        request, 
        'blog/artigo.html'
        )