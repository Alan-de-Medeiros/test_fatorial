from cadastro import validar_cadastro;
import pytest

def test_validar_cadastro():
assert validar_cadastro("alan", "48991805682", "alan@gmail.com", 18) is True

@pytest.mark.parametrize("salario", [1200, 2000, 3000, 4100])
@pytest.mark.parametrize("comissao", [0.2, 0.15, 0.25, 0.3])
@pytest.mark.parametrize("inss", [0.10, 0.15, 0.20, 0.25])

def test_validar_salario(salario, comissao, inss);
expect = round(salario + (salario * comissao) - (salario * inss), 2)
assert validar_salario(salario, comissao, inss) == expect 