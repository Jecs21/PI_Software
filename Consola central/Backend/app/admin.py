from django.contrib import admin
from .models import *

# Register your models here.

class Consolas(admin.ModelAdmin):
    list_display=('Consola_id','Consola_client')
    list_display_links = ('Consola_id','Consola_client')

class Unidades(admin.ModelAdmin):
    list_display=('Unidade_id','Unidade_consola','Unidade_sensor')
    list_display_links = ('Unidade_consola','Unidade_sensor')

class Dados(admin.ModelAdmin):
    list_display=('data_time','data_value','data_Unidade')
    list_display_links = ('data_time','data_value','data_Unidade')

admin.site.register(ConsolaCentral,Consolas)
admin.site.register(UnidadeSensorial,Unidades)
admin.site.register(Dados_unidades,Dados)