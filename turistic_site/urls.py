"""turistic_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from pontos_turisticos.api.viewsets import TuristicPointViewSet
from atracoes.api.viewsets import AtracaoViewSet
from comentarios.api.viewsets import CommentViewSet
from avaliacoes.api.viewsets import ReviewViewSet
from localizacao.api.viewsets import LocalizationViewSet

router = routers.DefaultRouter()
router.register(r'pontoturistico', TuristicPointViewSet)
router.register(r'atracoes', AtracaoViewSet)
router.register(r'comentarios', CommentViewSet)
router.register(r'avaliacaos', ReviewViewSet)
router.register(r'localizacao', LocalizationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
