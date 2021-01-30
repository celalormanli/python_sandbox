from src.sandbox import Sandbox


def test_fibonacci():
    sandbox = Sandbox()
    assert sandbox.fibonacci(1) == 1
    assert sandbox.fibonacci(10) == 55
