from django.db import models


class EmpresaModels(models.Model):

    nome_empresa = models.CharField(
        max_length=30, verbose_name="Nome", blank=False, null=False
    )
    logo_fundo_claro_empresa = models.ImageField(
        upload_to="imagens_empresa",
        blank=False,
        null=False,
        verbose_name="Logo para fundo claro (300x80)",
    )
    logo_fundo_escuro_empresa = models.ImageField(
        upload_to="imagens_empresa",
        blank=False,
        null=False,
        verbose_name="Logo para fundo escuro (300x80)",
    )
    instagram_empresa = models.CharField(
        max_length=255,
        verbose_name="Instagram (Link)",
        default=None,
        null=True,
        blank=True,
    )
    whatsapp_empresa = models.CharField(
        max_length=11,
        verbose_name="WhatsApp (Apenas numeros com DDD)",
        default=None,
        null=True,
        blank=True,
    )
    facebook_empresa = models.CharField(
        max_length=255,
        verbose_name="Facebook (Link)",
        default=None,
        null=True,
        blank=True,
    )
    youtube_empresa = models.CharField(
        max_length=255,
        verbose_name="YouTube (Link)",
        default=None,
        null=True,
        blank=True,
    )
    email_empresa = models.CharField(
        max_length=255, verbose_name="Email", default=None, null=True, blank=True
    )
    publicado_empresa = models.BooleanField(verbose_name="Publicado", default=False)

    def __str__(self):
        return self.nome_empresa

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresa"
