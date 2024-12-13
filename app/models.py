from django.db import models
class Funcionario(models.Model):
    nome = models.CharField(max_length=100, null= False, blank=False)
    cpf = models.CharField(max_length=14, null= False, blank=False, default='0')
    email = models.EmailField(null=False, blank=False)
    remuneracao = models.DecimalField(decimal_places=2, max_digits=8, null=False, blank=False, default='0')
