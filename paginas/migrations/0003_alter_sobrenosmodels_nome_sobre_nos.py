# Generated by Django 5.0.4 on 2024-05-18 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("paginas", "0002_alter_funcionariomodels_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sobrenosmodels",
            name="nome_sobre_nos",
            field=models.CharField(
                default="Sobre Nós", max_length=50, verbose_name="Página"
            ),
        ),
    ]
