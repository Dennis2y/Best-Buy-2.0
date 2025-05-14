import pytest
from products import Product

# Test: Creating a valid product
def test_create_product():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active()

# Test: Creating a product with empty name should raise exception
def test_create_product_empty_name():
    with pytest.raises(Exception):
        Product("", price=1450, quantity=100)

# Test: Creating a product with negative price should raise exception
def test_create_product_negative_price():
    with pytest.raises(Exception):
        Product("MacBook Air M2", price=-10, quantity=100)

# Test: Product becomes inactive when quantity reaches 0
def test_product_becomes_inactive_when_out_of_stock():
    product = Product("Test Product", price=100, quantity=1)
    product.buy(1)
    assert not product.is_active()

# Test: Buying product decreases quantity correctly and returns correct total
def test_product_buy_correctly():
    product = Product("Keyboard", price=100, quantity=5)
    total = product.buy(3)
    assert total == 300
    assert product.quantity == 2

# Test: Buying more than available quantity raises exception
def test_buy_more_than_available():
    product = Product("Mouse", price=50, quantity=2)
    with pytest.raises(Exception):
        product.buy(5)
