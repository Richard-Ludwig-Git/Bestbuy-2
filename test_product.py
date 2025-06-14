import pytest
from product import Product


def test_create_product():
    assert isinstance(Product("Flasche", price=0.13, quantity=12), Product)


def test_invalid_name():
    with pytest.raises(Exception, match="Name is not allowed to be empty"):
        Product(price=0.13, quantity=12)
    with pytest.raises(Exception, match="Price could not be negative"):
        Product(name="Flasche", price=-5, quantity=12)
    with pytest.raises(Exception, match="Quantity could not be negative"):
        Product(name="Flasche", price=5, quantity=-12)


def test_zero_inactive():
    flasch = Product("Flasche", price=0.13, quantity=12)
    flasch.set_quantity(0)
    assert not flasch.is_active()


def test_purchase_works():
    flasch = Product("Flasche", price=0.13, quantity=12)
    assert flasch.buy(10) == 1.30
    assert flasch.get_quantity() == 2


def test_buy_over_quantity():
    flasch = Product("Flasche", price=0.13, quantity=12)
    with pytest.raises(Exception, match="Quantity to high, not enough in Stock"):
        flasch.buy(13)



