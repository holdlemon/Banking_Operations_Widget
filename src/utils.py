import csv
import json
import logging
import os
from typing import Dict, List

import pandas as pd

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"../logs/{__name__}.log", mode="w")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def get_transactions_json(path: str) -> List[Dict]:
    """ Возвращает список словарей, содержащих данные об транзакциях"""
    if not os.path.exists(path):
        logger.error("Файл пустой")
        return []

    try:
        logger.info("Получаем данные о транзакциях в формате JSON")
        with open(path, "r", encoding="utf-8") as file:
            transaction = json.load(file)

    except json.JSONDecodeError as ex:
        logger.error(f"Произошла ошибка в файле формата JSON: {ex}")
        return []

    if not isinstance(transaction, list):
        logger.error("Некорректный тип данных в файле формата JSON")
        return []

    return transaction


def get_transactions_csv(path: str) -> List[Dict] | str:
    """ Получает данные об транзакциях из CSV файла """
    list_transactions = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            read_csv = csv.DictReader(file, delimiter=";")
            for item in read_csv:
                list_transactions.append(item)

            return list_transactions
    except FileNotFoundError as ex:
        return f"Файл не найден: {ex}"


def get_transactions_xlsx(path: str) -> list[dict] | str:
    """ Получает данные об транзакциях из XLSX файла"""
    try:
        with open(path, "rb") as file:
            read_xlsx = pd.read_excel(file)
            read_xlsx_to_dict = read_xlsx.to_dict(orient="records")

            return read_xlsx_to_dict
    except FileNotFoundError as ex:
        return f"Файл не найден: {ex}"


# if __name__ == "__main__":
#     file_path = "../data/operations.json"
#     print(get_transactions_json(file_path))
#     file_path = "../data/transactions_excel.xlsx"
#     print(get_transactions_xlsx(file_path))
