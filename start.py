from settings import dp
from aiogram.utils import executor
from views import register_handlers_view

register_handlers_view(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
