from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='fornecedores/logos/', null=True, blank=True)
    estado = models.CharField(max_length=50)
    custo_por_kwh = models.DecimalField(max_digits=5, decimal_places=2)
    limite_minimo_kwh = models.PositiveIntegerField()
    num_total_clientes = models.PositiveIntegerField()
    avaliacao_media = models.FloatField()

    def __str__(self):
        return self.nome
