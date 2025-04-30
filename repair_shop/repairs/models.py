from django.db import models

# Create your models here.
from django.db import models

class Equipment(models.Model):
    BRAND_CHOICES = [
        ('APPLE', 'Apple'),
        ('SAMSUNG', 'Samsung'),
        ('LG', 'LG'),
        ('SONY', 'Sony'),
        ('MOTOROLA', 'Motorola'),
        ('ASUS', 'Asus'),
        ('ACER', 'Acer'),
        ('DELL', 'Dell'),
        ('HP', 'HP'),
        ('LENOVO', 'Lenovo'),
        ('OUTRAS', 'OUTRAS'),
    ]

    TYPE_CHOICES = [
        ('CELULAR', 'Celular'),
        ('TABLET', 'Tablet'),
        ('NOTEBOOK', 'Notebook'),
        ('CAMERA', 'Câmera'),
        ('TV', 'Televisor'),
        ('SOM', 'Aparelho de Som'),
        ('MICROONDAS', 'Microondas'),
        ('OUTROS','OUTROS'),
    ]

    id = models.AutoField(primary_key=True)
    description = models.CharField('Descrição', max_length=200)
    brand = models.CharField('Marca', max_length=50, choices=BRAND_CHOICES)
    model = models.CharField('Modelo', max_length=100)
    serial_number = models.CharField('Número Serial', max_length=100)
    equipment_type = models.CharField('Tipo', max_length=50, choices=TYPE_CHOICES)
    entry_date = models.DateField('Data de Entrada')
    exit_date = models.DateField('Data de Saída', null=True, blank=True)
    defect_description = models.TextField('Descrição do Defeito')
    repair_description = models.TextField('Descrição do Reparo')
    observations = models.TextField('Observações', blank=True)

    class Meta:
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'

    def __str__(self):
        return f"{self.brand} {self.model} - {self.serial_number}" 