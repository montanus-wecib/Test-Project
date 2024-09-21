import main
import pytest

@pytest.fixture
def key():
    return main.testo(2)

def test_1(key):
    assert key

def test_2(key):
    assert isinstance(key, tuple)

def test_3(key):
    assert len(key) == 3

def test_4(key):
    assert key == (2, 4, 8)

