from data import DataForTestBun


class TestBun:

    def test_get_name_success(self, test_bun):        
        check_name = test_bun.get_name()

        assert check_name == DataForTestBun.bun_name


    def test_get_price_success(self, test_bun):
        check_price = test_bun.get_price()

        assert check_price == DataForTestBun.bun_price
