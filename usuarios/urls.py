from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from mysticareaapp.views import index,cartomantes,criar_cartomantes, editar, deletar
from .views import criar_usuario


urlpatterns = [
	path('login/', auth_views.LoginView.as_view(template_name = 'usuarios/form_login.html'), name = 'login'), 
	path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
	path('criar_usuario/', criar_usuario, name = 'criar_usuario'),
]