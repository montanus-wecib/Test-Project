# Imports
import sys
import os

# Add the root directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import main  # Now you can import main
import pytest

@pytest.fixture
def key():
    return main.testo(2)

def test_(key):
    assert isinstance(key, tuple)
