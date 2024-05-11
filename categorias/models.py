from django.db import models


class EstadoDeConservacaoModels(models.Model):
    nome_estado_de_conservacao = models.CharField(
        max_length=50, verbose_name="Estado de Conservação"
    )
    imagem_estado_de_conservacao = models.ImageField(
        upload_to="imagens_estado_de_conservacao",
        blank=True,
        null=True,
        verbose_name="Imagem do quadrado na Home (400x250)",
    )

    def __str__(self):
        return self.nome_estado_de_conservacao

    class Meta:
        verbose_name = "Estado de Conservação"
        verbose_name_plural = "Estados de Conservação"


class CategoriaModels(models.Model):
    nome_categoria = models.CharField(max_length=50, verbose_name="Categoria")

    def __str__(self):
        return self.nome_categoria

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class MarcaModels(models.Model):
    nome_marca = models.CharField(max_length=50, verbose_name="Marca")

    def __str__(self):
        return self.nome_marca

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"


class CorModels(models.Model):
    nome_cor = models.CharField(max_length=50, verbose_name="Cor")

    def __str__(self):
        return self.nome_cor

    class Meta:
        verbose_name = "Cor"
        verbose_name_plural = "Cores"


class CambioModels(models.Model):
    nome_cambio = models.CharField(max_length=50, verbose_name="Câmbio")

    def __str__(self):
        return self.nome_cambio

    class Meta:
        verbose_name = "Câmbio"
        verbose_name_plural = "Câmbios"
