from django.contrib.auth.models import User
from django.http.response import HttpResponse
from rest_framework import generics, permissions, renderers
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404

from .serializers import *
from .models import *

from django.shortcuts import render

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        try: 
            id = request.query_params["id"]
            print(id)
            if id!= None:
                user = User.objects.get(id=id)
                serializer = UserSerializer(user) 
        except:
            users = User.objects.all()
            users = self.get_queryset()
            serializer = UserSerializer(users, many = True)
        
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        user_data = request.data
        new_user = User.objects.create(username = user_data['username'] , email = user_data ['email'], password = user_data['password'])
        new_user.save()
        serializer = UserSerializer(new_user)
    
        return Response(serializer.data)

class UserDetail(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
###


class ConsolaList(generics.ListAPIView):
    queryset = ConsolaCentral.objects.all()
    serializer_class = ConsolasSerializer

    def get(self, request, *args, **kwargs):
        try: 
            Consola_id = request.query_params["Consola_id"]
            print(Consola_id)
            if Consola_id!= None:
                Consola = ConsolaCentral.objects.get(Consola_id=Consola_id)
                serializer = ConsolasSerializer(Consola,many = False)
        except:
            consolas = ConsolaCentral.objects.all()
            consolas = self.get_queryset()
            serializer = ConsolasSerializer(consolas, many =True)
        
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        consola_data = request.data
        new_consola = ConsolaCentral.objects.create(Consola_client = User.objects.get(id = consola_data["Consola_client"]))
        new_consola.save()
        serializer = ConsolasSerializer(new_consola)  
        return Response(serializer.data)


class UnidadesList(generics.ListAPIView):
    queryset = UnidadeSensorial.objects.all()
    serializer_class = UnidadesSerializer

    def post(self, request, *args, **kwargs):
        unidade_data = request.data
        new_unidade = UnidadeSensorial.objects.create(Unidade_sensor = unidade_data["Unidade_sensor"], Unidade_consola= ConsolaCentral.objects.get(Consola_id = unidade_data ["Unidade_consola"]))
        new_unidade.save()
        serializer = UnidadesSerializer(new_unidade)  
        return Response(serializer.data)
    
    #def get (self, request, *args, **kwargs):
    #    return UnidadeSensorial.objects.filter(Unidade_consola_id=self.kwargs['pk'])[0]

class UnidadesDetail(generics.RetrieveAPIView):
    serializer_class = UnidadesSerializer

    def get (self, request, *args, **kwargs):
        queryset = UnidadeSensorial.objects.filter(Unidade_consola_id=self.kwargs['pk'])
        return queryset

class DadosList(generics.ListAPIView):
    queryset = Dados_unidades.objects.all()
    serializer_class = DadosSerializer
