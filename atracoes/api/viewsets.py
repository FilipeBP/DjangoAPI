#from django_filters.rest_framework import DjangoFilterBackend ; Caso queira que apenas as aplicações selecionadas possuam esse tipo de filtro.
from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializers import AtracaoSerializer

class AtracaoViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    #filter_backends = (DjangoFilterBackend,)
    filter_fileds = ['name','description','min_age']