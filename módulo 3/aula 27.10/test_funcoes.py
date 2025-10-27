from funcoes import somar, subtrair, processar_lista

import pytest
def test_somar_positivos():
    assert somar(10,5)== 15

def test_subtrair_negativos():
    assert subtrair(5,10)== -5

def test_processar_lista_ordenacao():
    lista_desordenada = [3,1,2,4]
    lista_esperada = [1,2,3,4]
    assert processar_lista(lista_desordenada) == lista_esperada
    with pytest.raises(ValueError) as e:
        processar_lista([])
    assert "Lista não pode ser vazia" in str(e.value)
