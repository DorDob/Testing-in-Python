import pytest
from src.factorial import factorial   # wszystko z src.factorial zaimportujemy gwiazdką "*"  (tzn.obiekty, funkcje, itd.)

@pytest.mark.parametrize(   # ten test wykona się tyle razy, ile wrzucimy tu zestawów danych/ Dekorator jest nadpisywany tylko na 1 metodę i tej właśnie metody wstawiamy nasze dane, np. argument a i wynik działania f-cji ,,result"
    "n,result",
 [
     (4,24),   # pomiędzi poszczególnymi tuplami zawierającymi dane (parametr,wynik) musimy umieścić przecinek
     (0,1),
     (-10, False)

 ]
)

def test_factorial (n, result):
    assert factorial(n) == result

# def test_add():
#     assert 1+1 == 2           wykonując powyższy zapis, po prostu skracamy sobie zapis poniżej i piszemy mniej kodu
#
# def test_positive(a,result):
#      assert factorial(a)==result
#
#
# def test_zero():
#     assert factorial(0) == 1
#
#
# def test_pnegative():  #ujemna wartość
#     assert factorial(-10) == False