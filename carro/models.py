from django.db import models
from categorias.models import EstadoDeConservacaoModels, CategoriaModels, MarcaModels, CorModels, CambioModels
from utils import utils


class CarroModels(models.Model):

    modelo = models.CharField(
        max_length=100, verbose_name='Modelo', default=None)
    estado_de_conservacao = models.ForeignKey(
        EstadoDeConservacaoModels, on_delete=models.DO_NOTHING, blank=False, null=False, default=None, verbose_name='Estado de Conservação')
    categoria = models.ForeignKey(
        CategoriaModels, on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Categoria')
    marca = models.ForeignKey(
        MarcaModels, on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Marca')
    ano = models.CharField(max_length=9, verbose_name='Ano', default=None)
    cor = models.ForeignKey(
        CorModels, on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Cor')
    quilometragem = models.PositiveIntegerField(
        verbose_name='Quilometragem', blank=False, null=False)
    motorizacao = models.CharField(
        max_length=20, verbose_name='Motorização', default=None)
    cambio = models.ForeignKey(
        CambioModels, on_delete=models.DO_NOTHING, blank=False, null=False, verbose_name='Câmbio')
    preco = models.FloatField(verbose_name='Preço',
                              default='0', blank=False, null=False)
    opcionais = models.TextField(
        verbose_name='Opcionais', blank=True, null=True)
    publicado = models.BooleanField(
        verbose_name='Publicado', default=False)
    destaque = models.BooleanField(
        verbose_name='Destaque', default=False)

    def get_preco_formatado(self):
        return utils.formata_preco_admin(self.preco)
    get_preco_formatado.short_description = "Preço"

    def get_quilometragem_formatado(self):
        return utils.formata_quilometragem(self.quilometragem)
    get_quilometragem_formatado.short_description = "Quilometragem"

    def __str__(self):
        return self.modelo

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'


class ImagesCarroModels(models.Model):

    carro = models.ForeignKey(CarroModels, on_delete=models.CASCADE)
    imagem = models.ImageField(
        upload_to='imagens_carro', blank=False, null=False, default=None, verbose_name='Imagem')

    def __str__(self):
        return self.carro.modelo

    class Meta:
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'
