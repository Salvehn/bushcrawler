import pytest
from typing import Iterable
from index import crawler, Bush


def test_crawler_small():
    with pytest.raises(ValueError,match=r"garden is too .*"):
        crawler([Bush(i) for i in range(2)])

def test_crawler_big():
    with pytest.raises(ValueError,match=r"garden is too .*"):
        crawler([Bush(i) for i in range(2147483647)])

def test_crawler_instance():
    with pytest.raises(ValueError,match=r"wrong bush grade"):
        crawler([i for i in range(214)])
