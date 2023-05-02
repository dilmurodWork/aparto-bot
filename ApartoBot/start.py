from settings import dp
from aiogram.utils import executor
from views import register_handlers_client

register_handlers_client(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
