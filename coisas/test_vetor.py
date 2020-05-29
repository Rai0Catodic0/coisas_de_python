from vetor import Vetor
from math import sqrt

def test_initialization():
    """
    Testa se o vetor seta as variáveis corretamente
    """

    v = Vetor(1, 2)

    assert v.x == 1
    assert v.y == 2


def test_eq():
    """
    Testa se igualdade funciona
    """

    v_a = Vetor(1, 2)
    v_b = Vetor(1, 2)
    v_c = Vetor(2, 1)

    assert v_a == v_b
    assert v_b == v_a
    assert v_c != v_a


def test_add():
    """
    Testa se soma funciona
    """
    v_a = Vetor(1, 2)
    v_b = Vetor(1, 2)
    v_c = Vetor(2, 1)

    v_ab = v_a + v_b
    assert v_ab.x == v_a.x + v_b.x
    assert v_ab.y == v_a.y + v_b.y

    v_abc = v_a + v_b + v_c
    assert v_abc.x == v_a.x + v_b.x + v_c.x
    assert v_abc.y == v_a.y + v_b.y + v_c.y


def test_abs():
    """
    testa se o operador abs funciona
    """
    v_a = Vetor(3, 4)
    v_b = Vetor(9, 16)
    abs_a = abs(v_a)
    assert abs_a == sqrt(v_a.x**2+v_a.y**2)
    abs_b = abs(v_b)
    assert abs_b == sqrt(v_b.x**2+v_b.y**2)
