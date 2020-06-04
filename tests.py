import pytest
from typing import Iterable
from index import crawler, Bush

def test_crawler_max():
    assert crawler('1 2 3 4 5') == 4

def test_crawler_small():
    with pytest.raises(ValueError,match=r"garden is too .*"):
        crawler('1 2')

def test_crawler_big():
    with pytest.raises(ValueError,match=r"garden is too .*"):
        crawler(' '.join([str(i) for i in range(1000)]))

def test_crawler_inputlen():
    with pytest.raises(ValueError,match=r"input str too short"):
        crawler('')

def test_crawler_digits():
    with pytest.raises(ValueError,match=r"incorrect user input"):
        crawler('f a 3 2')
