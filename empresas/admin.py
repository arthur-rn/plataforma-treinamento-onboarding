from django.contrib import admin
from .models import Empresa


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    #Colunas que vão aparecer na tabela de listagem
    list_display = ('nome', 'slug', 'cnpj', 'cor_primaria', 'ativo', 'criado_em')
    
    #Barra de busca por nome ou CNPJ
    search_fields = ('nome', 'cnpj')
    
    #Filtro lateral por status ativo/inativo
    list_filter = ('ativo', 'criado_em')
    
    #Preenche o slug em tempo real enquanto você digita o nome
    prepopulated_fields = {'slug': ('nome',)}