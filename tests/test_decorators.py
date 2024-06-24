import pytest

from src.decorators import log, my_function


def test_log():

    with pytest.raises(Exception):
        my_function()
