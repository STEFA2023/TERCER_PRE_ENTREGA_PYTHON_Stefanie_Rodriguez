"""
URL configuration for Tercer_pre_entrega project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
import Tercer_pre_entrega.views
from AppRecetasBlog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio),
    path('crear_recetas/',agregar_receta),
    path('recetas/', ver_recetas_ingresadas),
    path('Login_usuario/', agregar_usuario),
    path('usuario/', ver_usuario_ingresado),
    path('ingreso_al_blog/', agregar_blog),
    path('blog/', ver_blog_ingresado),
    path('sobre_mi/', sobre_mi),
]
