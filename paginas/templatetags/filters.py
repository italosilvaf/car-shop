import os

from django.conf import settings
from django.template import Library
from PIL import Image

from carro.models import CarroModels
from utils import utils

register = Library()


@register.filter
def formata_preco(valor):
    return utils.formata_preco(valor)


@register.filter
def formata_preco_admin(valor):
    return utils.formata_preco_admin(valor)


@register.filter
def formata_quilometragem(valor):
    return utils.formata_quilometragem(valor)


@register.filter
def formata_celular(valor):
    return utils.formata_celular(valor)


@register.filter
def contar_carros_categoria(cat):
    contagem = len(
        CarroModels.objects.filter(
            categoria_carro__nome_categoria__iexact=cat, publicado=True
        )
    )
    return contagem


@register.simple_tag
def criar_favicon_atraves_da_logo(image_path):
    try:
        full_image_path = os.path.join(settings.MEDIA_ROOT, image_path)

        img = Image.open(full_image_path)

        max_size = 144

        width, height = img.size

        if width > height:
            new_width = max_size
            new_height = int((max_size / width) * height)
        else:
            new_height = max_size
            new_width = int((max_size / height) * width)

        resized_img = img.resize((new_width, new_height), Image.ANTIALIAS)

        favicon_name = f"favicon_{os.path.basename(image_path)}"
        favicon_path = os.path.join(settings.MEDIA_ROOT, favicon_name)

        resized_img.save(favicon_path, format="PNG")

        return os.path.join(settings.MEDIA_URL, favicon_name)

    except Exception:
        return image_path
