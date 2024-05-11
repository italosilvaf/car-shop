# Generated by Django 5.0.4 on 2024-05-04 11:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("categorias", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CarroModels",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "modelo",
                    models.CharField(
                        default=None, max_length=100, verbose_name="Modelo"
                    ),
                ),
                (
                    "ano",
                    models.CharField(default=None, max_length=9, verbose_name="Ano"),
                ),
                (
                    "quilometragem",
                    models.PositiveIntegerField(verbose_name="Quilometragem"),
                ),
                (
                    "motorizacao",
                    models.CharField(
                        default=None, max_length=20, verbose_name="Motorização"
                    ),
                ),
                ("preco", models.FloatField(default="0", verbose_name="Preço")),
                (
                    "opcionais",
                    models.TextField(blank=True, null=True, verbose_name="Opcionais"),
                ),
                (
                    "publicado",
                    models.BooleanField(default=False, verbose_name="Publicado"),
                ),
                (
                    "destaque",
                    models.BooleanField(default=False, verbose_name="Destaque"),
                ),
                (
                    "cambio",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="categorias.cambiomodels",
                        verbose_name="Câmbio",
                    ),
                ),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="categorias.categoriamodels",
                        verbose_name="Categoria",
                    ),
                ),
                (
                    "cor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="categorias.cormodels",
                        verbose_name="Cor",
                    ),
                ),
                (
                    "estado_de_conservacao",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="categorias.estadodeconservacaomodels",
                        verbose_name="Estado de Conservação",
                    ),
                ),
                (
                    "marca",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="categorias.marcamodels",
                        verbose_name="Marca",
                    ),
                ),
            ],
            options={
                "verbose_name": "Carro",
                "verbose_name_plural": "Carros",
            },
        ),
        migrations.CreateModel(
            name="ImagesCarroModels",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "imagem",
                    models.ImageField(
                        default=None, upload_to="imagens_carro", verbose_name="Imagem"
                    ),
                ),
                (
                    "carro",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="carro.carromodels",
                    ),
                ),
            ],
            options={
                "verbose_name": "Imagem",
                "verbose_name_plural": "Imagens",
            },
        ),
    ]
