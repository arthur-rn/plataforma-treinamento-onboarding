from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Cargo


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'empresa', 'criado_em')
    search_fields = ('nome', 'empresa__nome')
    list_filter = ('empresa',)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    #Colunas na listagem de usuários
    list_display = ('email', 'first_name', 'last_name', 'empresa', 'cargo', 'tipo', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name', 'empresa__nome')
    list_filter = ('tipo', 'empresa', 'is_staff', 'is_active')
    ordering = ('email',)

    #Adicionar nossos campos personalizados (empresa, cargo, tipo, telefone) nas telas de edição
    fieldsets = UserAdmin.fieldsets + (
        ('Informações da Empresa e Cargo', {
            'fields': ('empresa', 'cargo', 'tipo', 'telefone')
        }),
    )

    #Adicionar nossos campos na tela de criação de novo usuário
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informações da Empresa e Cargo', {
            'fields': ('email', 'first_name', 'last_name', 'empresa', 'cargo', 'tipo', 'telefone')
        }),
    )