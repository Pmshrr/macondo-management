import sales

def test_find_latte():
    result = sales.find_drink("latte")
    assert result == {"drink": "latte", "price": 200000}
def test_find_unknown_drink():
    result = sales.find_drink("pizza")
    assert result is None
def test_find_espresso():
    result = sales.find_drink("espresso")
    assert result == {"drink": "espresso", "price": 140000}
def test_find_americano():
    result = sales.find_drink("americano")
    assert result == {"drink": "americano", "price": 150000}
def test_find_case_sensitivity():
    result = sales.find_drink("LATTE")
    assert result is None