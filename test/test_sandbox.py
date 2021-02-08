from src.sandbox import Sandbox


def test_fibonacci():
    sandbox = Sandbox()
    assert sandbox.fibonacci(1) == 1
    assert sandbox.fibonacci(10) == 55


def test_tower_of_hanoi():
    src = [4, 3, 2, 1]
    aux = []
    dest = []
    sandbox = Sandbox()
    sandbox.tower_of_hanoi(4, src, dest, aux)
    assert dest == [4, 3, 2, 1]
    assert aux == []
    assert src == []
