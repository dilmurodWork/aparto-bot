from aiogram import Bot
from aiogram import Dispatcher
import configparser
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext


config = configparser.ConfigParser()
config.read("./config.ini")
token = str(config['Telegram']['bot_token'])
phone = config['Telegram']['phone']
chanel_id = config['Telegram']['chanel_id']

bot = Bot(token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
