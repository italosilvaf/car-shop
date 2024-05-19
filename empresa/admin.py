from django.contrib import admin

from .models import EmpresaModels


class EmpresaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nome_empresa",
        "logo_empresa",
        "instagram_empresa",
        "whatsapp_empresa",
        "facebook_empresa",
        "youtube_empresa",
    )
    list_display_links = ("id", "nome_empresa")


admin.site.register(EmpresaModels, EmpresaAdmin)
