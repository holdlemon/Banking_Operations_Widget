import unittest
from unittest.mock import patch, MagicMock


from src.external_api import convert_transaction_to_rubles

# Предполагаемые URL и API_KEY для запросов
URL = "https://api.example.com/exchange_rates"
API_KEY = "your_api_key_here"


class TestConvertTransactionToRubles(unittest.TestCase):
    @patch('requests.get')
    def test_convert_rub_to_rub(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"rates": {"RUB": 1.0}}
        mock_get.return_value = mock_response

        transaction = {"amount": "100", "currency": "RUB"}
        result = convert_transaction_to_rubles(transaction)
        self.assertEqual(result, 100.0)

    @patch('requests.get')
    def test_convert_usd_to_rub(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"rates": {"RUB": 70.0}}
        mock_get.return_value = mock_response

        transaction = {"amount": "100", "currency": "USD"}
        result = convert_transaction_to_rubles(transaction)
        self.assertEqual(result, 7000.0)

    @patch('requests.get')
    def test_convert_eur_to_rub(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"rates": {"RUB": 80.0}}
        mock_get.return_value = mock_response

        transaction = {"amount": "100", "currency": "EUR"}
        result = convert_transaction_to_rubles(transaction)
        self.assertEqual(result, 8000.0)

    @patch('requests.get')
    def test_convert_gbp_to_rub(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"rates": {"RUB": 90.0}}
        mock_get.return_value = mock_response

        transaction = {"amount": "100", "currency": "GBP"}
        result = convert_transaction_to_rubles(transaction)
        self.assertEqual(result, 9000.0)

    @patch('requests.get')
    def test_api_error(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_get.return_value = mock_response

        transaction = {"amount": "100", "currency": "USD"}
        with self.assertRaises(Exception):
            convert_transaction_to_rubles(transaction)
