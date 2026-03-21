class TestBun:

    def test_get_name_success(self, test_bun):        
        check_name = test_bun.get_name()

        assert check_name == 'Ржаная'


    def test_get_price_success(self, test_bun):
        check_price = test_bun.get_price()

        assert check_price == 30
