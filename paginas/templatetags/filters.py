from django.template import Library
from utils import utils
from carro.models import CarroModels

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
def contar_carros_categoria(cat):
    contagem = len(CarroModels.objects.filter(
        categoria_carro__nome_categoria__iexact=cat, publicado=True
    )
    )
    return contagem
