import pytest
from unittest.mock import Mock
from unittest.mock import patch
from bun import Bun
from ingredient import Ingredient



class TestBurger:

    def test_set_buns_success(self, test_burger):
        mock_bun = Mock(spec=Bun)
        mock_bun.name = 'Лаваш'
        mock_bun.price = 25
        test_burger.set_buns(mock_bun)
        
        assert test_burger.bun.name == 'Лаваш'
        assert test_burger.bun.price == 25

   
    @pytest.mark.parametrize('type, name, price', [[1, 2, 3],
                                                   ['Начинка', 'Петрушка', 'пять рублей'],
                                                   [1.5, 2.5, 3.5]])
    def test_add_ingredient_success(self, test_burger, type, name, price):
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.ingredient_type = type
        mock_ingredient.name = name
        mock_ingredient.price = price
        test_burger.add_ingredient(mock_ingredient)
        
        assert test_burger.ingredients[0].ingredient_type == type
        assert test_burger.ingredients[0].name == name
        assert test_burger.ingredients[0].price == price
        assert test_burger.ingredients[0] == mock_ingredient


    def test_remove_ingredient_remove_success(self, test_burger):
        mock_ingredient_1 = Mock(spec=Ingredient)
        mock_ingredient_2 = Mock(spec=Ingredient)
        test_burger.ingredients.append(mock_ingredient_1)
        test_burger.ingredients.append(mock_ingredient_2)
        test_burger.remove_ingredient(0)       

        assert test_burger.ingredients[0] == mock_ingredient_2
        assert len(test_burger.ingredients) == 1

    
    def test_remove_ingredient_empty_list_failed(self, test_burger):
        try:
            test_burger.remove_ingredient(0)
        except IndexError as e:        
            assert str(e) == "list assignment index out of range"

          
    def test_move_ingredient_move_succes(self, test_burger):
        mock_ingredient_1 = Mock(spec=Ingredient)
        mock_ingredient_2 = Mock(spec=Ingredient)        
        test_burger.ingredients.append(mock_ingredient_1)
        test_burger.ingredients.append(mock_ingredient_2)
        test_burger.move_ingredient(0,1)

        assert test_burger.ingredients[0] == mock_ingredient_2
        assert len(test_burger.ingredients) == 2

    
    @patch('bun.Bun', autospec=True)
    @patch('ingredient.Ingredient', autospec=True)
    def test_get_price_succes(self, mock_bun, mock_ingredient, test_burger):
        mock_bun.get_price.return_value = 30.4
        mock_ingredient.get_price.return_value = 20.5
        test_burger.bun = mock_bun
        test_burger.ingredients.append(mock_ingredient)
        check_price = test_burger.get_price()
 
        assert check_price == 81.3
                

    @patch('bun.Bun', autospec=True)
    @patch('ingredient.Ingredient', autospec=True)
    @patch('burger.Burger.get_price', return_value = 90)
    def test_get_receipt(self, mock_bun, mock_ingredient, mock_burger, test_burger):
        mock_bun.get_name.return_value = 'Булочка с кунжутом'
        mock_ingredient.get_type.return_value = 'Начинка'
        mock_ingredient.get_name.return_value = 'Огурцы, салат и лук'
        test_burger.bun = mock_bun
        test_burger.ingredients.append(mock_ingredient)
        check_receipt = test_burger.get_receipt()
 
        assert check_receipt == '(==== Булочка с кунжутом ====)\n= начинка Огурцы, салат и лук =\n(==== Булочка с кунжутом ====)\n\nPrice: 90'
