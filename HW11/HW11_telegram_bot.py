from dotenv import load_dotenv
import os
import telebot
import requests

load_dotenv("/Users/andrykozlovets/Documents/\
PRJCT Python Beginner/HM/gifs.env")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GIPHY_API_KEY = os.getenv("GIPHY_API_KEY")


# Search GIFs
def search_gifs(api_key, query):
    url = "https://api.giphy.com/v1/gifs/search"
    params = {
        "api_key": api_key,
        "q": query,
        "limit": 3
    }
    response = requests.get(url, params=params)
    data = response.json()
    gifs = [item['images']['original']['url'] for item in data['data']]
    return gifs


# Initialization telegram bot
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


# The function that will be called by the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Send me a search word and \
I will find GIFs for you.")


# The function that will be called when the user sends a message
@bot.message_handler(func=lambda message: True)
def search(message):
    query = message.text
    gifs = search_gifs(GIPHY_API_KEY, query)
    for gif in gifs:
        bot.send_message(message.chat.id, gif)


# Starting the telegram bot
bot.polling(none_stop=True)
