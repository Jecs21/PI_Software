from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from django.contrib.auth.models import User

class ConsolaCentral(models.Model):
    Consola_id = models.AutoField(auto_created=True,primary_key=True)
    Consola_client = models.ForeignKey(User,on_delete=models.CASCADE)
       
class UnidadeSensorial(models.Model):
    Unidade_id = models.AutoField(auto_created=True,primary_key=True)
    Unidade_consola = models.ForeignKey(ConsolaCentral,on_delete=models.CASCADE)
    Unidade_sensor = models.CharField(max_length=100)

class Dados_unidades(models.Model):
    data_time = models.DateTimeField(default=timezone.now)
    data_value = models.IntegerField(default=0)
    data_Unidade = models.ForeignKey(UnidadeSensorial,on_delete=models.CASCADE)