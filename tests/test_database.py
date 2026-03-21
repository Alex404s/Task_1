from bun import Bun
from ingredient import Ingredient
from unittest.mock import Mock


class TestDatabase:

    def test_available_buns_list_view_success(self, test_database):
        mock_bun_1 = Mock(spec=Bun)
        mock_bun_2 = Mock(spec=Bun)
        test_database.buns = [mock_bun_1, mock_bun_2]     

        assert test_database.available_buns() == [mock_bun_1, mock_bun_2]        


    def test_available_buns_check_name_first_el_success(self, test_database):
        mock_bun_1 = Mock(spec=Bun)
        mock_bun_1.name = 'Бородинская'
        mock_bun_2 = Mock(spec=Bun)       
        test_database.buns = [mock_bun_1, mock_bun_2]

        assert test_database.buns[0].name == 'Бородинская'
        

    def test_available_buns_check_price_first_el_success(self, test_database):
        mock_bun_1 = Mock(spec=Bun)        
        mock_bun_1.price = 40
        mock_bun_2 = Mock(spec=Bun)        
        test_database.buns = [mock_bun_1, mock_bun_2]
       
        assert test_database.buns[0].price == 40
        

    def test_available_buns_check_name_sec_el_success(self, test_database):
        mock_bun_1 = Mock(spec=Bun)
        mock_bun_2 = Mock(spec=Bun)
        mock_bun_2.name = 'Пшеничная'
        test_database.buns = [mock_bun_1, mock_bun_2]     

        assert test_database.buns[1].name == 'Пшеничная'


    def test_available_buns_check_price_sec_el_success(self, test_database):
        mock_bun_1 = Mock(spec=Bun)       
        mock_bun_2 = Mock(spec=Bun)        
        mock_bun_2.price = 25
        test_database.buns = [mock_bun_1, mock_bun_2]  

        assert test_database.buns[1].price == 25


    def test_available_ingredients_view_success(self, test_database):
        mock_ingredient_1 = Mock(spec=Ingredient)        
        mock_ingredient_2 = Mock(spec=Ingredient)       
        test_database.ingredients = [mock_ingredient_1, mock_ingredient_2]     

        assert test_database.available_ingredients() == [mock_ingredient_1, mock_ingredient_2]        
        

    def test_available_ingredients_check_type_first_el_success(self, test_database):
        mock_ingredient_1 = Mock(spec=Ingredient)
        mock_ingredient_1.ingredient_type = 'соус'        
        mock_ingredient_2 = Mock(spec=Ingredient)       
        test_database.ingredients = [mock_ingredient_1, mock_ingredient_2]
        
        assert test_database.ingredients[0].ingredient_type == 'соус'
        

    def test_available_ingredients_check_name_first_el_success(self, test_database):
        mock_ingredient_1 = Mock(spec=Ingredient)        
        mock_ingredient_1.name = 'кетчуп'        
        mock_ingredient_2 = Mock(spec=Ingredient)        
        test_database.ingredients = [mock_ingredient_1, mock_ingredient_2]
       
        assert test_database.ingredients[0].name == 'кетчуп'


    def test_available_ingredients_check_price_first_el_success(self, test_database):
        mock_ingredient_1 = Mock(spec=Ingredient)        
        mock_ingredient_1.price = 30
        mock_ingredient_2 = Mock(spec=Ingredient)        
        test_database.ingredients = [mock_ingredient_1, mock_ingredient_2]   

        assert test_database.ingredients[0].price == 30     


    def test_available_ingredients_check_type_sec_el_success(self, test_database):
        mock_ingredient_1 = Mock(spec=Ingredient)        
        mock_ingredient_2 = Mock(spec=Ingredient)
        mock_ingredient_2.ingredient_type = 'соус'
        test_database.ingredients = [mock_ingredient_1, mock_ingredient_2]

        assert test_database.ingredients[1].ingredient_type == 'соус'


    def test_available_ingredients_check_name_sec_el_success(self, test_database):
        mock_ingredient_1 = Mock(spec=Ingredient)
        mock_ingredient_2 = Mock(spec=Ingredient)  
        mock_ingredient_2.name = 'майонез'

        test_database.ingredients = [mock_ingredient_1, mock_ingredient_2]  

        assert test_database.ingredients[1].name == 'майонез'


    def test_available_ingredients_check_price_sec_el_success(self, test_database):
        mock_ingredient_1 = Mock(spec=Ingredient)        
        mock_ingredient_2 = Mock(spec=Ingredient)       
        mock_ingredient_2.price = 20
        test_database.ingredients = [mock_ingredient_1, mock_ingredient_2]     

        assert test_database.ingredients[1].price == 20
    