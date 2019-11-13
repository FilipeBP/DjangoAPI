from rest_framework.viewsets import ModelViewSet
from pontos_turisticos.models import TuristicPoint
from .serializers import TuristicPointSerializer

class TuristicPointViewSet(ModelViewSet):
    queryset = TuristicPoint.objects.all()
    serializer_class = TuristicPointSerializer
