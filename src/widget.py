from datetime import datetime

from src.masks import mask_account, mask_card


def mask_data(data: str) -> str:
    """ Маскирует номер карты/счета в зависимости от типа """

    name = []
    number = []
    for i in data:
        if i.isalpha():
            name.append(i)
        elif i.isdigit():
            number.append(i)

    if len(number) == 16:
        return f"{"".join(name)} {mask_card(int("".join(number)))}"
    else:
        return f"{"".join(name)} {mask_account(int("".join(number)))}"


def convert_date(date: str) -> str:
    """ Конвертирует дату """
    cor_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    cor_date_str = datetime.strftime(cor_date, "%d.%m.%Y")
    return cor_date_str
