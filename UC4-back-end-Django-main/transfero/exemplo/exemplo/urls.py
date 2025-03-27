from django.contrib import admin
from django.urls import include, path
#biblioteca do método HttpResponse

from django.http import HttpResponse
#from blog import views as views_blog
from home import views as views_home
from contato import views as views_contato


#funções para carregar views diretamente





urlpatterns = [
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('blog/', include('blog.urls')),
    #path('blog/', views_blog.blog),
    path('contato/', views_contato.contato),
    path('admin/', admin.site.urls),
]
