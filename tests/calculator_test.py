from src.calculator import Calculator
import pytest  

calc = Calculator()                         #  Calculator  to obiekt


@pytest.mark.parametrize(
    "a,b,result",
    [
        (1, 2, 3),
        (0, 0, 0),
        (-1, -2, -3)
    ]

)  # wykonam 3 iteracje testujące poprawność działania metody (każda iteracja, sprawdza poprawność działania 1 zestawu danych (a,b i rezultat działania f-cji)
def test_add(a, b, result): 
    assert calc.add(a, b) == result

# def test_add1():  # działanie podpinam pod odrębne definicje, jeżeli chce zobaczyć wyniki dla odrębnych działań
#     assert calc.add(-1,1) == 0

# def test_add(a,b,result):
#     assert calc.add(a,b) == result



