from src.masks import mask_card, mask_account


def test_mask_card(card):
    assert mask_card(card) == "7000 67** **** 0987"


def test_mask_account(account):
    assert mask_account(account) == "**4305"
