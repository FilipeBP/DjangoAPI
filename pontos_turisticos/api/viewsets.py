from rest_framework.viewsets import ModelViewSet
from pontos_turisticos.models import TuristicPoint
from .serializers import TuristicPointSerializer
from rest_framework.decorators import action

class TuristicPointViewSet(ModelViewSet):
    queryset = TuristicPoint.objects.all()
    serializer_class = TuristicPointSerializer

    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    def get_queryset(self):
        id = self.request.query_params.get('id', None) #Busca pelo id passado, caso não encontre, retorna None.
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = TuristicPoint.objects.all() #Lazyload, ou seja, apenas há a preparação do load ods objetos.

        #Do jeito que está abaixo, a busca está procurando um objeto que possua TODAS as características passadas
        if id:
            queryset = TuristicPoint.object.filter(pk=id)
        if nome:
            queryset = queryset.filter(nome__iexact=nome) #Se o nome for igual ao do queryset criado em 'id', o queryset retorna o objeto que contaham os parâmetros passados.
        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao) #Com o __iexact, o parâmetro deixa de ser case sensitive

        return queryset
