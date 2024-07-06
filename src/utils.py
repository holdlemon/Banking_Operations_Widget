import json
import logging
import os
from typing import Dict, List


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"logs/{__name__}.log", mode="w")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def get_transactions(path: str) -> List[Dict]:
    """ Возвращает список словарей, содержащих данные об транзакциях"""
    if not os.path.exists(path):
        logger.error("Файл пустой")
        return []

    try:
        logger.info("Получаем данные о транзакциях")
        with open(path, "r", encoding="utf-8") as file:
            transaction = json.load(file)

    except json.JSONDecodeError as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return []

    if not isinstance(transaction, list):
        logger.error("Некорректный тип данных")
        return []

    return transaction


if __name__ == "__main__":
    file_path = "../data/operations.json"
    print(get_transactions(file_path))
