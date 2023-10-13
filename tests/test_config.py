import pytest

class NotInRange(Exception):
    def __init__(self,message="value not in range"):
        self.message = message
        super().__init__(self.message)
        

def test_generic1():       # name should start with "test_"
    a=5
    b=10
    assert a<b            


def test_generic2():       # name should start with "test_"
    a=2
    with pytest.raises(NotInRange):
        if a not in range(4,8):
            raise NotInRange  