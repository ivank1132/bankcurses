import requests

url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&json"
data = requests.get(url).json()
usd_rate = data[0]["rate"]
print("--- Онлайн-обмінник (UAH -> USD) ---")
print("Для вихода введіть 'exit'")
while True:
    user_input = input("\nВведіть суму в грн (UAH): ").strip()
    if user_input.lower() == 'exit':
        break
    try:
        uah_amount = float(user_input.replace(',', '.'))
        usd_amount = uah_amount / usd_rate
        print(f"Результат: {usd_amount:.2f} USD (по курсу НБУ: {usd_rate:.2f})")
    except ValueError:
        print("Будь ласка, напишіть конкретне число")