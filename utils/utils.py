import re

def formata_preco(valor):
    return f"{valor:_.2f}".replace(".", ",").replace("_", ".")


def formata_preco_admin(valor):
    return f"R$ {valor:_.2f}".replace(".", ",").replace("_", ".")


def formata_quilometragem(valor):
    return f"{valor:,} Km".replace(",", ".")


def formata_celular(valor):
    regex = r'(\d{2})(\d{5})(\d{4})'
    return re.sub(regex, r'(\1) \2-\3', valor)
