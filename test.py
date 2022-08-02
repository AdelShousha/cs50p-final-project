import requests

response = requests.get(f"https://api.quran.com/api/v4/quran/verses/uthmani?verse_key=36%3A1")
print(response.json()["verses"][0]["text_uthmani"])


