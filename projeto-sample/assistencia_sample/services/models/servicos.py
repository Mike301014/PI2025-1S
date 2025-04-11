from django.db import models


class Servicos(models.Model):

    id_service = models.AutoField(primary_key=True)
    nm_service = models.CharField(max_length=80, blank=False, null=False)
    price = models.FloatField()
    status = models.CharField(max_length=30, blank=False, null=False)
    dt_start = models.DateTimeField()
    dt_end = models.DateField()
    desc = models.TextField()