
from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        #fields = ['id', 'username']
        fields = ['id', 'username', 'email', 'password']
class ConsolasSerializer(serializers.ModelSerializer):  
    #Consola_client = UserSerializer(many=False, read_only=True)
    class Meta:
        model = ConsolaCentral
        #exclude = []
        fields = ['Consola_id','Consola_client']
        #depth =1
class UnidadesSerializer(serializers.ModelSerializer):

    class Meta: 
        model = UnidadeSensorial
        #exclude = []
        fields = ['Unidade_id','Unidade_sensor','Unidade_consola']
        #depth =1 -> Unidade_Consola associada ao id da consola

class DadosSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Dados_unidades
        exclude = []
        #fields = ['data_time','data_value','data_Unidade']
