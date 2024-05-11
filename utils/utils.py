def formata_preco(valor):
    return f"{valor:_.2f}".replace(".", ",").replace("_", ".")


def formata_preco_admin(valor):
    return f"R$ {valor:_.2f}".replace(".", ",").replace("_", ".")


def formata_quilometragem(valor):
    return f"{valor:,} Km".replace(",", ".")
