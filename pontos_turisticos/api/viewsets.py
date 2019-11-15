from rest_framework.viewsets import ModelViewSet
from pontos_turisticos.models import TuristicPoint
from .serializers import TuristicPointSerializer
import rest_framework.decorators.actions

class TuristicPointViewSet(ModelViewSet):
    queryset = TuristicPoint.objects.all()
    serializer_class = TuristicPointSerializer

    @action(method=['get'], detail=True)
    def denunciar(self, request, pk=None):

