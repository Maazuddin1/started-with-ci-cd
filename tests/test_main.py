from src.main import add

def test_add_funtion():
    assert add(1,2) == 3
    assert add(0,0) == 0
    assert add(-1,-1) == -2
    assert add(1,-1) == 0
    assert add(1,0) == 1
    assert add(10,11) == 21