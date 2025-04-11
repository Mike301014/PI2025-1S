from django.db import models


class Estoque(models.Model):

    id_produto = models.AutoField(primary_key=True)
    nm_produto = models.CharField(max_length=80, blank=False, null=False)
    price = models.FloatField()
    tp_produto = models.CharField(max_length=80)
    