from rest_framework import serializers
from .models import Questoes

class QuestaoSerializer(serializers.Serializer):
    class Meta:
        model = Questoes
        fields = ('pergunta', 'descricao')