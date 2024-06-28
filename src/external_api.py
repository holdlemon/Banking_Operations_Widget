import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

URL = "https://api.apilayer.com/exchangerates_data/latest"
load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_exchange_rate(base_currency: str, target_currency: str = "RUB") -> Any:
    """ Получаем курс валют к рублю """

    headers = {"apikey": API_KEY}
    params = {"base": base_currency, "symbols": target_currency}
    response = requests.get(URL, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        return data["rates"][target_currency]
    else:
        raise Exception(f"Ошибка запроса {response.status_code}")


def convert_transaction_to_rubles(transaction: Dict) -> Any:
    """ Конвертируем в рубли """
    amount = transaction["amount"]
    currency = transaction["currency"]
    if currency == "RUB":
        return float(amount)
    else:
        exchange_rate = get_exchange_rate(currency)
        return round(exchange_rate * float(amount), 2)


# Пример использования
if __name__ == "__main__":
    example_transaction = {
        'amount': 100,
        'currency': 'USD'
    }
    rubles_amount = convert_transaction_to_rubles(example_transaction)
    print(f"Transaction amount in RUB: {rubles_amount}")
