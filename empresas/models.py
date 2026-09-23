from django.db import models
from django.utils.text import slugify


class Empresa(models.Model):
    nome = models.CharField('Nome da Empresa', max_length=150)
    slug = models.SlugField('Identificador na URL', max_length=150, unique=True, blank=True)
    cnpj = models.CharField('CNPJ', max_length=18, blank=True, null=True)
    
    #Identidade Visual (White-Label)
    logo = models.ImageField('Logo da Empresa', upload_to='empresas/logos/', blank=True, null=True)
    cor_primaria = models.CharField('Cor Primária (Hex)', max_length=7, default='#2563EB', help_text='Ex: #2563EB (Azul)')
    cor_secundaria = models.CharField('Cor Secundária (Hex)', max_length=7, default='#1E40AF', help_text='Ex: #1E40AF')
    
    #Controle
    ativo = models.BooleanField('Ativo', default=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['nome']

    def __str__(self):
        return self.nome

    #Método para gerar um slug baseado no nome caso o mesmo não seja preenchido 
    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)