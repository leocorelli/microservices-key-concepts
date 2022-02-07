from logic import add, sub
import pytest

def test_add():
    assert 2 == add(1,1)

def test_sub():
    assert 7 == pytest.approx(sub(10,3))