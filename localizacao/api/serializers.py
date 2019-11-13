from rest_framework.serializers import ModelSerializer
from localizacao.models import Localization

class LocalizationSerializer(ModelSerializer):
    class Meta:
        model = Localization
        fields = ('id','country','state','city','row1','row2','lat','long')