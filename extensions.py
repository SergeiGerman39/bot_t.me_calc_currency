import requests
import json
from config import currencies


class APIException(Exception):
    pass


class Convertor:
    @staticmethod
    def get_price(base_key, to_key, amount):
        try:
            base = currencies[base_key.lower()]
        except KeyError:
            return APIException(f'Валюта {base_key} не найдена')
        try:
            sym = currencies[to_key.lower()]
        except KeyError:
            raise APIException(f'Валюта {to_key} не найдена')

        if base == sym:
            raise APIException(f'Две одинаковые валюты {base_key} конвертировать невозможно!')

        try:
            amount = float(amount.replace(",", "."))
        except ValueError:
            raise APIException(f'Введённое количество валюты {amount} обработать на удалось!')

        url = f"https://api.apilayer.com/exchangerates_data/latest?symbols={sym}&base={base}"

        payload = {}
        headers = {
            "apikey": "0D6jarTZtAIl4gzf5sG00nW9lQt4Wz5a"
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        resp = json.loads(response.content)
        new_amount = resp['rates'][sym] * float(amount)
        return new_amount
