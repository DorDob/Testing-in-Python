import pytest
from src.rest_from_division import rest_from_division


@pytest.mark.parametrize(
    "a,x,result",
 [
     (-2,8,6),
     (-1,10,9),
     (10,2,0),
     (3,2,1),
     (9,30,9)
 ]
)

def test_rest_from_division(a,x,result):
    assert rest_from_division(a,x) == result