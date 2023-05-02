from aiogram import Bot
from aiogram import Dispatcher
import configparser


config = configparser.ConfigParser()
config.read("./config.ini")
token = config['Telegram']['bot_token']
token = str(token)


bot = Bot(token)
dp = Dispatcher(bot)
