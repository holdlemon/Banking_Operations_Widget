import pytest

from src.decorators import my_function


def test_log():

    with pytest.raises(Exception):
        my_function()
