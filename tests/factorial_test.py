import pytest
from src.factorial import factorial   

@pytest.mark.parametrize(  
    "n,result",
 [
     (4,24),   
     (0,1),
     (-10, False)
 ]
)


def test_factorial (n, result):
    assert factorial(n) == result
