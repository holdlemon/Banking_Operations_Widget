import re
from collections import Counter
from typing import Any, Dict, List


def filter_by_state(list_of_dict: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """ Возвращает список словарей со значением ключа state """

    result = []
    for dictionary in list_of_dict:
        if dictionary["state"] == state:
            result.append(dictionary)
    return result


def sort_by_date(list_of_dict: List[Dict[str, Any]], ascending: bool = True) -> List[Dict[str, Any]]:
    """ Возвращает отсортированный список словарей по дате """

    return sorted(list_of_dict, key=lambda x: x["date"], reverse=ascending)


def search_by_description(operations: list[dict], user_search: str) -> list[dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска
    и возвращает список словарей, у которых в описании есть данная строка
    """

    return [operation for operation in operations if re.search(user_search.lower(), operation["description"].lower())]


def get_count_operations_by_category(operations: list[dict], list_of_category: list) -> dict:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций
    и возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории
    """
    result = Counter(
        [operation["description"] for operation in operations if operation["description"] in list_of_category]
    )

    return dict(result)
