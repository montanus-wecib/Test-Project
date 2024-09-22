import main
import pytest

@pytest.fixture
def key():
    return main.testo(2)

def test_3(key):
    assert len(key) == 3
