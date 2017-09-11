from django.db import models

# class Relatorio(models.Model):

'''
    Relatório 1
'''
class AcompanhamentoCantina(models.Model):
    data = models.DateField()
    responsavel_preenchimento = models.CharField(max_length=100, blank=False)
    responsavel_informacao = models.CharField(max_length=100, blank=False)
    escola = models.CharField(max_length=100, blank=False)
    nome_cantineiro = models.CharField(max_length=100, blank=False)
    resposta_alimentos = models.CharField(max_length=200, blank=False)
    #relatorio = models.ForeignKey(Relatorio, on_delete=models.CASCADE)

class AvaliacaoCantina(models.Model):
    pergunta = models.CharField(max_length=50, blank=False)
    resposta_avaliacao = models.CharField(max_length=3, blank=False)
    acompanhamento = models.ForeignKey(AcompanhamentoCantina, on_delete=models.CASCADE)


'''
    Relatório 2

class AcompanhamentoAlgumaCoisa(models.Model):
    resposta_alimentos = models.CharField(max_length=200, blank=False)
    relatorio = models.ForeignKey(Relatorio, on_delete=models.CASCADE)

class AvaliacaoAlgumaCoisa(models.Model):
    pergunta = models.CharField(max_length=50, blank=False)
    resposta_avaliacao = models.CharField(max_length=3, blank=False)
    observacao = models.CharField(max_length=100, blank=True)
    acompanhamento = models.ForeignKey(AcompanhamentoCantina, on_delete=models.CASCADE)



'''
    #Relatório 3
'''
class AcompanhamentoAlgumaCoisa2(models.Model):
    resposta_alimentos = models.CharField(max_length=200, blank=False)
    relatorio = models.ForeignKey(Relatorio, on_delete=models.CASCADE)

class AvaliacaoAlgumaCoisa2(models.Model):

    acompanhamento = models.ForeignKey(AcompanhamentoCantina, on_delete=models.CASCADE)    
'''