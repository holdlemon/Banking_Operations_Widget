def mask_card(number_card: int) -> str:
    """Возвращает маску номера карты"""

    return f"{str(number_card)[:4]} {str(number_card)[4:6]}** **** {str(number_card)[12:]}"


def mask_account(number_account: int) -> str:
    """Возвращает маску номера счета"""

    return f"**{str(number_account)[-4:]}"
