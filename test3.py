import main
import pytest

@pytest.fixture
def key():
    return main.testo(2)

def test_(key):
    assert key == (2, 4, 8)
