from django.db import models
from models import Servicos


class Transacao(models.Model):

    id_transacao = models.AutoField(primary_key=True)
    service = models.ForeignKey(Servicos, on_delete=models.CASCADE)
    price = models.FloatField()
    tp_transacao = models.CharField(max_length=30, blank=False, null=False)
    dt_transaca = models.DateField()
    desc = models.TextField