import pytest
from .bun import Bun
from .ingredient import Ingredient

@pytest.fixture
def test_bun():
    test_bun = Bun('Ржаная', 30)
    return test_bun

@pytest.fixture
def test_ingredient():
    test_ingredient = Ingredient('Соус', 'Сычуаньский', 50)
    return test_ingredient