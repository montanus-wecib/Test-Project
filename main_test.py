import main
import pytest

def test_main():
  assert main.squareit(2) == 3

if __name__ == "__main__":
  test_main():
