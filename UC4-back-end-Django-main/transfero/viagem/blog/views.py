from django.shortcuts import render
from requests import request
from rest_framework import viewsets
from blog.serializers import TopicoSerializer
from blog.models import Topico

# Create your views here.
def blog(request):
    contexto = {
        'titulo' : 'Jornada Viagem | Blog'
    }
    return render(request, 
                  'blog/index.html',
                  contexto,
                  )

class TopicoViewSet(viewsets.ModelViewSet):
    queryset = Topico.objects.all()
    serializer_class = TopicoSerializer


def artigos(request):
    exibe_artigos = {
    'titulo' : 'Jornada Viagem | Blog',
    'artigos' : Topico.objects.all()
}

    return render(
    request,
    'blog/tabela.html',
    exibe_artigos,
)