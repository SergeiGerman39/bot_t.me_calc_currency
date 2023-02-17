import requests
import json

base_key = 'PLN'
to_key = 'RUB'
amount = 12000

url = f"https://api.apilayer.com/exchangerates_data/latest?symbols={to_key}&base={base_key}"

payload = {}
headers= {
  "apikey": "0D6jarTZtAIl4gzf5sG00nW9lQt4Wz5a"
}

response = requests.request("GET", url, headers=headers, data = payload)
resp = json.loads(response.content)
new_amount = resp['rates'][to_key]*float(amount)
print(new_amount)