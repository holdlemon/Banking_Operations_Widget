import pytest

from src.widget import mask_data, convert_date


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Visa Platinum 7000 7922 8960 6361", "VisaPlatinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Visa Classic 6831982476737658", "VisaClassic 6831 98** **** 7658"),
    ],
)
def test_mask_data(value, expected):
    assert mask_data(value) == expected


def test_convert_date(date):
    assert convert_date(date) == "11.07.2018"
