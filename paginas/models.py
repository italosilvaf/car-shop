from django.db import models


class HomeModels(models.Model):

    nome_home = models.CharField(
        max_length=50, verbose_name='Página',  blank=False, null=False, default='Home')
    titulo_home = models.CharField(
        max_length=15, verbose_name='Título',  blank=True, null=True, default=None)
    subtitulo_home = models.CharField(
        max_length=30, verbose_name='Subtítulo',  blank=True, null=True, default=None)
    descricao_home = models.TextField(
        max_length=65, verbose_name='Descrição', blank=True, null=True, default=None)
    publicado_home = models.BooleanField(
        verbose_name='Publicado', default=False)
    imagem_home = models.ImageField(
        upload_to='imagens_home', blank=True, null=True, verbose_name='Background (1920x803)', default=None)

    def __str__(self):
        return self.nome_home

    class Meta:
        verbose_name = 'Presonalização da página Home'
        verbose_name_plural = 'Presonalização da página Home'


class QualidadesHomeModels(models.Model):

    nome_qualidade = models.CharField(
        max_length=20, verbose_name='Qualidade', blank=False, null=False, default='')
    descricao_qualidade = models.TextField(
        max_length=70, verbose_name='Descrição da qualidade', blank=True, null=True, default=None)
    publicado_qualidade = models.BooleanField(
        verbose_name='Publicado', default=False)
    icon_qualidade = models.ImageField(
        upload_to='imagens_home/icon_qualidades', blank=False, verbose_name='Icon (75x75)', null=False, default=None)

    def __str__(self):
        return self.nome_qualidade

    class Meta:
        verbose_name = 'Qualidade'
        verbose_name_plural = 'Qualidades'

from email.policy import default
from django.db import models


class SobreNosModels(models.Model):

    nome_sobre_nos = models.CharField(
        max_length=50, verbose_name='Página',  blank=False, null=False, default='About')
    titulo_sobre_nos = models.CharField(
        max_length=50, verbose_name='Título',  blank=True, null=True, default=None)
    imagem_sobre_nos = models.ImageField(
        upload_to='imagens_sobre_nos/imagens_background', blank=True, null=True, verbose_name='Background (1920x400)')
    publicado_sobre_nos = models.BooleanField(
        verbose_name='Publicado', default=False)
    titulo_texto_sobre_nos = models.CharField(
        max_length=50, verbose_name='Título do texto',  blank=True, null=True, default=None)
    subtitulo_texto_sobre_nos = models.CharField(
        max_length=50, verbose_name='Subtítulo do texto',  blank=True, null=True, default=None)
    texto_sobre_nos = models.TextField(
        max_length=100000, verbose_name='Texto', blank=True, null=True, default=None)
    imagem_texto_um_sobre_nos = models.ImageField(
        upload_to='imagens_sobre_nos/imagens_texto_um', blank=True, null=True, default=None, verbose_name='Imagem do quadrado 1 (400x500)')
    imagem_texto_dois_sobre_nos = models.ImageField(
        upload_to='imagens_sobre_nos/imagens_texto_dois', blank=True, null=True, default=None, verbose_name='Imagem do quadrado 2 (400x500)')
    imagem_texto_tres_sobre_nos = models.ImageField(
        upload_to='imagens_sobre_nos/imagens_texto_tres', blank=True, null=True, default=None, verbose_name='Imagem do quadrado 3 (400x500)')

    def __str__(self):
        return self.nome_sobre_nos

    class Meta:
        verbose_name = 'Presonalização da página Sobre Nós'
        verbose_name_plural = 'Presonalização da página Sobre Nós'


class FuncionarioModels(models.Model):

    nome = models.CharField(
        max_length=20, verbose_name='Nome', blank=False, null=False, default=' ')
    cargo = models.CharField(
        max_length=20, verbose_name='Cargo', blank=True, null=True, default=' ')
    publicado = models.BooleanField(
        verbose_name='Publicado', default=False)
    link_insta = models.CharField(max_length=1000000, verbose_name='Link do Instagram',
                                  blank=True, null=True, default=None)
    link_whats = models.CharField(max_length=1000000, verbose_name='Link do WhatsApp',
                                  blank=True, null=True, default=None)
    link_face = models.CharField(max_length=1000000, verbose_name='Link do Facebook',
                                 blank=True, null=True, default=None)
    foto = models.ImageField(upload_to='imagens_sobre_nos/imagens_funcionarios',
                             blank=False, null=False, default=' ', verbose_name='Foto (400x442)')

    def __str__(self):
        return self.nome


class EstoqueModels(models.Model):

    nome_estoque = models.CharField(
        max_length=50, verbose_name='Página',  blank=False, null=False, default='Estoque')
    titulo_estoque = models.CharField(
        max_length=40, verbose_name='Título',  blank=True, null=True, default=None)
    imagem_estoque = models.ImageField(
        upload_to='imagens_estoque/imagens_background', blank=True, null=True, default=None, verbose_name='Background (1920x400)')
    publicado_estoque = models.BooleanField(
        verbose_name='Publicado', default=False)

    def __str__(self):
        return self.nome_estoque

    class Meta:
        verbose_name = 'Presonalização da página Estoque'
        verbose_name_plural = 'Presonalização da página Estoque'