from rest_framework import serializers
from models import AcompanhamentoCantina, AvaliacaoCantina

class AvaliacaoCantinaSerializer(serializers.ModelSerializer):
    models = AvaliacaoCantina
    fields = ('pergunta', 'resposta_avaliacao')

class AcompanhamentoSerializer(serializers.ModelSerializer):
    avaliacoes = AvaliacaoCantinaSerializer(many=True, read_only:True)

    class Meta:
        models = AcompanhamentoCantina
        fields = (
            'data', 
            'responsavel_preenchimento',
            'responsavel_informacao',
            'escola',
            'nome_cantineiro',
            'resposta_alimentos',
            'avaliacoes')