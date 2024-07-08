import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"../logs/src.masks.log", mode="w")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def mask_card(number_card: int) -> str:
    """Возвращает маску номера карты"""
    logger.info("Маскируем номер карты")
    return f"{str(number_card)[:4]} {str(number_card)[4:6]}** **** {str(number_card)[12:]}"


def mask_account(number_account: int) -> str:
    """Возвращает маску номера счета"""
    logger.info("Маскируем номер счета")
    return f"**{str(number_account)[-4:]}"
