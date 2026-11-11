"""Regras de negócio do LocalEats."""

VALOR_MINIMO_DESCONTO = 100
PERCENTUAL_DESCONTO = 0.10


def calcular_desconto(valor_pedido):
    """Retorna o valor do desconto (não o valor final do pedido).

    - abaixo de R$ 100,00: sem desconto (0)
    - a partir de R$ 100,00: 10% de desconto
    - valores negativos: ValueError
    """
    if valor_pedido < 0:
        raise ValueError("O valor do pedido não pode ser negativo.")
    if valor_pedido < VALOR_MINIMO_DESCONTO:
        return 0
    return valor_pedido * PERCENTUAL_DESCONTO
