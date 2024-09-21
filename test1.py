import main
import pytest

@pytest.fixture
def key():
    return main.testo(2)

def test_1(key):
    assert key
