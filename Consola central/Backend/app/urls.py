from collections import UserList
from django.urls import path
from django.urls import include
from rest_framework import routers,serializers, viewsets
from rest_framework.urlpatterns import format_suffix_patterns
from . import views # . = current directory

#router = routers.DefaultRouter()
#router.register(r'users', UserList)

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('consolas/', views.ConsolaList.as_view(), name='Consola-List'),
    path('consolas/<int:pk>/', views.ConsolaDetail.as_view()),
    path('Unidades/', views.UnidadesList.as_view(), name='Unidades-List'),
    path('Unidades/<int:pk>/', views.UnidadesDetail.as_view()),
    path('Unidades/<str:pk>/', views.UnidadesDetail2.as_view()),
    path('Dados/', views.DadosList.as_view(), name='Dados-List'),
    path('Dados/<int:pk>', views.DadosDetail.as_view())
]

# optional
urlpatterns = format_suffix_patterns(urlpatterns)