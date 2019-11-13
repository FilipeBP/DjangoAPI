from rest_framework.serializers import ModelSerializer
from comentarios.models import Comment

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ()