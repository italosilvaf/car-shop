from django.contrib import admin
from .models import EstadoDeConservacao, Categoria, Marca, Cor, Cambio


class EstadoDeConservacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_estado_de_conservacao')
    list_display_links = ('id', 'nome_estado_de_conservacao')


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_categoria')
    list_display_links = ('id', 'nome_categoria')


class MarcaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_marca')
    list_display_links = ('id', 'nome_marca')


class CorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_cor')
    list_display_links = ('id', 'nome_cor')


class CambioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_cambio')
    list_display_links = ('id', 'nome_cambio')


admin.site.register(EstadoDeConservacao, EstadoDeConservacaoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Cor, CorAdmin)
admin.site.register(Cambio, CambioAdmin)
