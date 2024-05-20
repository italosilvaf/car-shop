from django.contrib import admin

from .models import EmpresaModels


class EmpresaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nome_empresa",
        "logo_fundo_claro_empresa",
        "logo_fundo_escuro_empresa",
        "instagram_empresa",
        "whatsapp_empresa",
        "facebook_empresa",
        "youtube_empresa",
        "publicado_empresa",
    )
    list_display_links = ("id", "nome_empresa")
    list_editable = ("publicado_empresa",)


admin.site.register(EmpresaModels, EmpresaAdmin)
