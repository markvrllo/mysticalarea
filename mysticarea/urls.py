"""mysticarea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.views.static import serve
from django.conf import settings
from django.views.generic.base import TemplateView
from mysticareaapp.views import index,cartomantes,criar_cartomantes, editar, deletar


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',TemplateView.as_view(template_name='cartomantes/index.html'), name= 'index'),
    path('cartomantes/', cartomantes, name = 'cartomantes'),
    path('criar_cartomantes/', criar_cartomantes, name = 'registrar_medium'),
    path('editar/<int:id>',editar, name = 'editar'),
    path('deletar/<int:id>',deletar, name = 'deletar'),
    path('', include('usuarios.urls')),
    url(r'^img/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)