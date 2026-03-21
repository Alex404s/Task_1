from data import DataFotTestIngredient


class TestIngredient:

    def test_get_price_success(self, test_ingredient):
        check_price = test_ingredient.get_price()

        assert check_price == DataFotTestIngredient.ingredient_price
   
   
    def test_get_name_success(self, test_ingredient):        
        check_name = test_ingredient.get_name()

        assert check_name == DataFotTestIngredient.ingredient_name    
    
    
    def test_get_type_success(self, test_ingredient):        
        check_type = test_ingredient.get_type()

        assert check_type == DataFotTestIngredient.ingredient_type


    
