from django.db import models

class EspecieModel(models.Model):
    nome_especie = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Espécie"
        verbose_name_plural = "Espécies"

    def __str__(self):
        return self.nome_especie