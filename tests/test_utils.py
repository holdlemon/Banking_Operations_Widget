import unittest
from unittest.mock import patch, mock_open


from src.utils import get_transactions


class TestGetTransaction(unittest.TestCase):

    @patch('os.path.exists')
    def test_file_not_exists(self, mock_exists):
        mock_exists.return_value = False
        result = get_transactions('nonexistent_file.json')
        self.assertEqual(result, [])

    @patch('os.path.exists')
    @patch('builtins.open', new_callable=mock_open, read_data='invalid json')
    def test_json_decode_error(self, mock_open_file, mock_exists):
        mock_exists.return_value = True
        result = get_transactions('invalid_json_file.json')
        self.assertEqual(result, [])

    @patch('os.path.exists')
    @patch('builtins.open', new_callable=mock_open, read_data='{"key": "value"}')
    def test_not_a_list(self, mock_open_file, mock_exists):
        mock_exists.return_value = True
        result = get_transactions('not_a_list_file.json')
        self.assertEqual(result, [])

    @patch('os.path.exists')
    @patch('builtins.open', new_callable=mock_open, read_data='[{"id": 1, "amount": 100}]')
    def test_valid_transaction_list(self, mock_open_file, mock_exists):
        mock_exists.return_value = True
        result = get_transactions('valid_transactions_file.json')
        self.assertEqual(result, [{"id": 1, "amount": 100}])
