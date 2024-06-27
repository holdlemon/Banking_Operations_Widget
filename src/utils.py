import json
import os
from typing import List, Dict


def get_transaction(path: str) -> List[Dict]:
    """ Возвращает список словарей, содержащих данные об транзакциях"""
    if not os.path.exists(path):
        return []

    try:
        with open(path, "r", encoding="utf-8") as file:
            transaction = json.load(file)

    except json.JSONDecodeError:
        return []

    if not isinstance(transaction, list):
        return []

    return transaction


if __name__ == "__main__":
    file_path = "../data/operations.json"
    print(get_transaction(file_path))
