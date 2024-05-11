from django.contrib import admin

from .models import (
    EstoqueModels,
    FuncionarioModels,
    HomeModels,
    QualidadesHomeModels,
    SobreNosModels,
)


class HomeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nome_home",
        "titulo_home",
        "subtitulo_home",
        "publicado_home",
    )
    list_display_links = ("id", "nome_home")
    list_editable = ("publicado_home",)


admin.site.register(HomeModels, HomeAdmin)


class QualidadesHomeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nome_qualidade",
        "descricao_qualidade",
        "publicado_qualidade",
    )
    list_display_links = ("id", "nome_qualidade")
    list_editable = ("publicado_qualidade",)


admin.site.register(QualidadesHomeModels, QualidadesHomeAdmin)


class SobreNosAdmin(admin.ModelAdmin):
    list_display = ("id", "nome_sobre_nos", "titulo_sobre_nos", "publicado_sobre_nos")
    list_display_links = ("id", "nome_sobre_nos")
    list_editable = ("publicado_sobre_nos",)


admin.site.register(SobreNosModels, SobreNosAdmin)


class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "cargo", "publicado")
    list_display_links = ("id", "nome")
    list_editable = ("publicado",)


admin.site.register(FuncionarioModels, FuncionarioAdmin)


class EstoqueAdmin(admin.ModelAdmin):
    list_display = ("id", "nome_estoque", "titulo_estoque", "publicado_estoque")
    list_display_links = ("id", "nome_estoque")
    list_editable = ("publicado_estoque",)


admin.site.register(EstoqueModels, EstoqueAdmin)
