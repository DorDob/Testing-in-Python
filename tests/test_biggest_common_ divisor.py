import pytest
from src.biggest_common_divisor import biggest_common_divisor

@pytest.mark.parametrize(
    "x,y,result",
 [
     (20,5,5),
     (30,7,1),
     (30,53,1),
     (75,25,25),
     (75,5,5)

 ]
)
def test_biggest_common_divisor(x,y,result):
    assert biggest_common_divisor(x,y) == result


