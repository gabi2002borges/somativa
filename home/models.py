from django.db import models

class Medico(models.Model):
    nome = models.CharField(max_length=20, default=None)
    crm = models.CharField(max_length=15)
    especialidade = models.CharField(max_length=60, default=None)
    foto = models.ImageField(blank=True, upload_to='foto_produto/%y/%m/%d/')
    mostrar = models.BooleanField(default=True)



