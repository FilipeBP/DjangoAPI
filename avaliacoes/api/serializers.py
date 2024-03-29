from rest_framework.serializers import ModelSerializer
from avaliacoes.models import Review

class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'user', 'comment', 'mark')