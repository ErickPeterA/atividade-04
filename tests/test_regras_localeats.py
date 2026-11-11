import pytest

from src.regras_localeats import calcular_desconto


# Responsável: Erick Peter
def test_pedido_de_150_recebe_desconto_de_10_por_cento():
    assert calcular_desconto(150) == pytest.approx(15)


# Responsável: Erick Peter
def test_pedido_abaixo_de_100_nao_recebe_desconto():
    assert calcular_desconto(80) == 0


# Responsável: Erick Peter (diferencial: borda + pytest.raises)
def test_pedido_de_exatamente_100_recebe_desconto():
    assert calcular_desconto(100) == pytest.approx(10)


# Responsável: Erick Peter (diferencial: pytest.raises)
def test_valor_negativo_gera_value_error():
    with pytest.raises(ValueError):
        calcular_desconto(-1)
