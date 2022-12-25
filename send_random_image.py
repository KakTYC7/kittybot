# kittybot/send_random_image.py
import requests
from telegram import Bot


bot = Bot(token='5895641824:AAEnBt8bZaYoUngciNZcRaZu9d71rKqKPxg')

URL = 'https://api.thecatapi.com/v1/images/search'
chat_id = 131276209

# Делаем GET-запрос к эндпоинту:
response = requests.get(URL).json()
# Извлекаем из ответа URL картинки:
random_cat_url = response[0].get('url')  

# Передаём chat_id и URL картинки в метод для отправки фото:
bot.send_photo(chat_id, random_cat_url)
