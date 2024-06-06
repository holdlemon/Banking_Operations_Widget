from typing import Any, Dict, List


def filter_by_state(list_of_dict: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    result = []
    for dictionary in list_of_dict:
        if dictionary["state"] == state:
            result.append(dictionary)
    return result


def sort_by_date(list_of_dict: List[Dict[str, Any]], ascending: bool = True) -> List[Dict[str, Any]]:
    return sorted(list_of_dict, key=lambda x: x["date"], reverse=ascending)
