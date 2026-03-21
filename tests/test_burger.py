import pytest
from unittest.mock import Mock
from unittest.mock import patch
from bun import Bun
from ingredient import Ingredient
from data import DataTestBurger



class TestBurger:

    def test_set_buns_name_success(self, test_burger):
        mock_bun = Mock(spec=Bun)
        mock_bun.name = 'Лаваш'
        test_burger.set_buns(mock_bun)
        
        assert test_burger.bun.name == 'Лаваш'        


    def test_set_buns_price_success(self, test_burger):
        mock_bun = Mock(spec=Bun)        
        mock_bun.price = 25
        test_burger.set_buns(mock_bun)        
        
        assert test_burger.bun.price == 25

   
    @pytest.mark.parametrize('type', [DataTestBurger.type_int_list])
    def test_add_ingredient_check_type_success(self, test_burger, type):
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.ingredient_type = type
        test_burger.add_ingredient(mock_ingredient)
        
        assert test_burger.ingredients[0].ingredient_type == type


    @pytest.mark.parametrize('name', [DataTestBurger.name_str_list])
    def test_add_ingredient_check_name_success(self, test_burger, name):
        mock_ingredient = Mock(spec=Ingredient)        
        mock_ingredient.name = name        
        test_burger.add_ingredient(mock_ingredient)        
        
        assert test_burger.ingredients[0].name == name        

    
    @pytest.mark.parametrize('price', [DataTestBurger.price_float_list])
    def test_add_ingredient_check_price_success(self, test_burger, price):
        mock_ingredient = Mock(spec=Ingredient)           
        mock_ingredient.price = price
        test_burger.add_ingredient(mock_ingredient)        
        
        assert test_burger.ingredients[0].price == price   


    def test_add_ingredient_success(self, test_burger):
        mock_ingredient = Mock(spec=Ingredient)
        test_burger.add_ingredient(mock_ingredient)        

        assert test_burger.ingredients[0] == mock_ingredient


    def test_remove_ingredient_remove_success(self, test_burger):
        mock_ingredient_1 = Mock(spec=Ingredient)
        mock_ingredient_2 = Mock(spec=Ingredient)
        test_burger.ingredients.append(mock_ingredient_1)
        test_burger.ingredients.append(mock_ingredient_2)
        test_burger.remove_ingredient(0)       

        assert test_burger.ingredients[0] == mock_ingredient_2
        assert len(test_burger.ingredients) == 1

          
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
