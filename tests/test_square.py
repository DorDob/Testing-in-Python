import pytest
from src.square import square

@pytest.mark.parametrize(
    "a,result",
 [

     (2,4),
     (9,81),
     (1.5,2.25),
     (27,729),
     (7,49)

 ]
)

def test_square(a,result):
    assert square(a) == result