import pytest
from bun import Bun
from ingredient import Ingredient
from burger import Burger
from database import Database
from data import *

@pytest.fixture
def test_bun():
    test_bun = Bun(DataForTestBun.bun_name, DataForTestBun.bun_price)
    return test_bun

@pytest.fixture
def test_ingredient():
    test_ingredient = Ingredient(DataFotTestIngredient.ingredient_type,
                                 DataFotTestIngredient.ingredient_name,
                                 DataFotTestIngredient.ingredient_price
                                )
    return test_ingredient

@pytest.fixture
def test_burger():
    test_burger = Burger()
    return test_burger

@pytest.fixture
def test_database():
    test_database = Database()
    return test_database