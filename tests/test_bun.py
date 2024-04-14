from praktikum.bun import Bun


class TestBun:
    def test_get_name_correct_name(self):
        bun = Bun('MegaBurger', 14)
        assert bun.get_name() == 'MegaBurger'

    def test_get_price_correct_price(self):
        bun = Bun('MegaBurger', 14)
        assert bun.get_price() == 14
