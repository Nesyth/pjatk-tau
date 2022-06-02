import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

######################################

@classmethod
def setup_class(cls):
    print('\n-- ADD SETUP --')

@classmethod
def teardown_class(cls):
    print('\n-- ADD TEARDOWN --')

add_param1 = [(1, 2, 3), (1, 1, 2), (3, 2, 5)]
add_param2 = [(753, 321, 1074), (555, 55, 610), (700, 77, 777)]
add_param3 = [(-10, -20, -30), (-5, -10, -15), (-999, -1, -1000)]
@pytest.mark.parametrize("num1, num2, result", add_param1)
def test_add(calc, num1, num2, result):
    assert calc.add(num1, num2) == result 

@pytest.mark.parametrize("num1, num2, result", add_param2)
def test_add2(calc, num1, num2, result):
    assert calc.add(num1, num2) == result   

@pytest.mark.parametrize("num1, num2, result", add_param3)
def test_addNegatives(calc, num1, num2, result):
    assert calc.add(num1, num2) == result

######################################

@classmethod
def setup_class(cls):
    print('\n-- MULTIPLY SETUP --')

@classmethod
def teardown_class(cls):
    print('\n-- MULTIPLY TEARDOWN --')

multiply_param1 = [(1, 2, 2), (1, 1, 1), (3, 2, 6)]
multiply_param2 = [(753, 321, 241713), (555, 55, 30525), (700, 77, 53900)]
multiply_param3 = [(-10, -20, 200), (5, -10, -50), (-999, 1, -999)]
@pytest.mark.parametrize("num1, num2, result", multiply_param1)
def test_multiply(calc, num1, num2, result):
    assert calc.multiply(num1, num2) == result 

@pytest.mark.parametrize("num1, num2, result", multiply_param2)
def test_multiply2(calc, num1, num2, result):
    assert calc.multiply(num1, num2) == result   

@pytest.mark.parametrize("num1, num2, result", multiply_param3)
def test_multiplyNegatives(calc, num1, num2, result):
    assert calc.multiply(num1, num2) == result

######################################

@classmethod
def setup_class(cls):
    print('\n-- DIVIDE SETUP --')

@classmethod
def teardown_class(cls):
    print('\n-- DIVIDE TEARDOWN --')

divide_param1 = [(1, 2, 0.5), (1, 1, 1), (3, 2, 1.5)]
divide_param2 = [(750, 150, 5), (555, 5, 111), (700, 1, 700)]
divide_param3 = [(-10, -20, 0.5), (5, -10, -0.5), (-999, 1, -999)]
@pytest.mark.parametrize("num1, num2, result", divide_param1)
def test_divide(calc, num1, num2, result):
    assert calc.divide(num1, num2) == result 

@pytest.mark.parametrize("num1, num2, result", divide_param2)
def test_divide2(calc, num1, num2, result):
    assert calc.divide(num1, num2) == result   

@pytest.mark.parametrize("num1, num2, result", divide_param3)
def test_divideNegatives(calc, num1, num2, result):
    assert calc.divide(num1, num2) == result