class TestIngredient:

    def test_get_price_success(self, test_ingredient):
        check_price = test_ingredient.get_price()

        assert check_price == 50   
   
   
    def test_get_name_success(self, test_ingredient):        
        check_name = test_ingredient.get_name()

        assert check_name == 'Сычуаньский'    
    
    
    def test_get_type_success(self, test_ingredient):        
        check_name = test_ingredient.get_type()

        assert check_name == 'Соус'


    
