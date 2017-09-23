from django.shortcuts import render
from .models import Questoes
from .serializers import QuestaoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET'])
def perguntas(request):
    questoes = Questoes.objects.all()

    print(questoes)

    if questoes:
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    else:
        serialize = QuestaoSerializer(questoes)
        return Response(serialize.data, status=status.HTTP_201_CREATED)


