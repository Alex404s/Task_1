from bun import Bun
from ingredient import Ingredient
from unittest.mock import Mock


class TestDatabase:

    def test_available_buns_list_view_success(self, test_database):
        mock_bun_1 = Mock(spec=Bun)
        mock_bun_1.name = 'Бородинская'
        mock_bun_1.price = 40
        mock_bun_2 = Mock(spec=Bun)
        mock_bun_2.name = 'Пшеничная'
        mock_bun_2.price = 25
        test_database.buns = [mock_bun_1, mock_bun_2]     

        assert test_database.available_buns() == [mock_bun_1, mock_bun_2]
        assert test_database.buns[0].name == 'Бородинская'
        assert test_database.buns[0].price == 40
        assert test_database.buns[1].name == 'Пшеничная'
        assert test_database.buns[1].price == 25

    def test_available_ingredients_view_success(self, test_database):
        mock_ingredient_1 = Mock(spec=Ingredient)
        mock_ingredient_1.ingredient_type = 'соус'
        mock_ingredient_1.name = 'кетчуп'
        mock_ingredient_1.price = 30
        mock_ingredient_2 = Mock(spec=Ingredient)
        mock_ingredient_2.ingredient_type = 'соус'
        mock_ingredient_2.name = 'майонез'
        mock_ingredient_2.price = 20
        test_database.ingredients = [mock_ingredient_1, mock_ingredient_2]     

        assert test_database.available_ingredients() == [mock_ingredient_1, mock_ingredient_2]
        assert test_database.ingredients[0].ingredient_type == 'соус'
        assert test_database.ingredients[0].name == 'кетчуп'
        assert test_database.ingredients[0].price == 30
        assert test_database.ingredients[1].ingredient_type == 'соус'
        assert test_database.ingredients[1].name == 'майонез'
        assert test_database.ingredients[1].price == 20