from django.contrib.auth.models import AbstractUser
from django.db import models
from empresas.models import Empresa


class Cargo(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='cargos', verbose_name='Empresa')
    nome = models.CharField('Nome do Cargo', max_length=100)
    descricao = models.TextField('Descrição das Responsabilidades', blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
        unique_together = ['empresa', 'nome']  #Não permite dois cargos com o mesmo nome na mesma empresa
        ordering = ['nome']

    def __str__(self):
        return f"{self.nome} ({self.empresa.nome})"


class CustomUser(AbstractUser):
    class TipoUsuario(models.TextChoices):
        SUPERADMIN = 'SUPERADMIN', 'Administrador da Plataforma'
        GESTOR = 'GESTOR', 'Gestor da Empresa'
        COLABORADOR = 'COLABORADOR', 'Novo Colaborador (Aluno)'

    #Login será realizado por email
    email = models.EmailField('E-mail', unique=True)
    
    #Relação com a Empresa e o Cargo
    empresa = models.ForeignKey(
        Empresa, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='usuarios',
        verbose_name='Empresa'
    )
    cargo = models.ForeignKey(
        Cargo, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='usuarios',
        verbose_name='Cargo'
    )
    tipo = models.CharField(
        'Tipo de Usuário', 
        max_length=20, 
        choices=TipoUsuario.choices, 
        default=TipoUsuario.COLABORADOR
    )
    telefone = models.CharField('Telefone / WhatsApp', max_length=20, blank=True)

    #Configuração para autenticação por e-mail:
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.email})"