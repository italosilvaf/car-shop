from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import CarroModels, ImagesCarroModels


class ImagesCarroInline(admin.TabularInline):
    model = ImagesCarroModels
    extra = 1


class CarroAdmin(SummernoteModelAdmin):
    list_display = (
        "id",
        "modelo",
        "cor",
        "ano",
        "get_quilometragem_formatado",
        "get_preco_formatado",
        "categoria",
        "publicado",
    )
    list_display_links = ("id", "modelo")
    list_editable = ("publicado",)
    inlines = [ImagesCarroInline]


admin.site.register(CarroModels, CarroAdmin)
admin.site.register(ImagesCarroModels)
