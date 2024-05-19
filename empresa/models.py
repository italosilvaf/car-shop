from django.db import models


class EmpresaModels(models.Model):

    nome_empresa = models.CharField(
        max_length=30, verbose_name="Nome", blank=False, null=False
    )
    logo_empresa = models.ImageField(
        upload_to="imagens_empresa", blank=False, null=False, verbose_name="Logo"
    )
    instagram_empresa = models.CharField(
        max_length=255, verbose_name="Instagram", default=None, null=True, blank=True
    )
    whatsapp_empresa = models.CharField(
        max_length=11, verbose_name="WhatsApp", default=None, null=True, blank=True
    )
    facebook_empresa = models.CharField(
        max_length=255, verbose_name="Facebook", default=None, null=True, blank=True
    )
    youtube_empresa = models.CharField(
        max_length=255, verbose_name="YouTube", default=None, null=True, blank=True
    )

    def __str__(self):
        return self.nome_empresa

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresa"
