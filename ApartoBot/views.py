from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from Keyboards.all_kb import *
from settings import bot
# from ChannelMessages import main

filters = {}
lang = ''
rus = '🇷🇺 Русский'
uzb = '🇺🇿 O\'zbekcha'

async def start(message: types.Message):
    text = 'Xush kelibsiz, tilni tanlang.\nДобро пожаловать выберите язык.'
    try:
        await bot.send_message(message.from_user.id, text, reply_markup=langs_kb)
        await message.delete()
        text = message.from_user.first_name
        text += ' запустил бот'
        await bot.send_message(chat_id=2039384031, text=text)
    except:
        await message.reply('Переход в ЛС, напишите ему:\nhttps://t.me/dnm_test_bot')

async def choose_language(message: types.Message):
    global lang
    lang = message.text
    if lang == rus:
        await message.reply(f"Выберите категорию ({lang}):", reply_markup= category_kb_ru)
    else:
        await message.reply(f"Kategoriyani tanlang ({lang}):", reply_markup= category_kb_uz)

async def choose_category(message: types.Message):
    filters['category'] = message.text
    if lang == rus:
        await message.reply(f"Выберите район ({message.text}):", reply_markup=district_kb_ru)
    else:
        await message.reply(f"Tumanni tanlang ({message.text}):", reply_markup=district_kb_uz)


async def choose_district(message: types.Message):
    district = message.text
    filters['district'] = district
    if lang == rus:
        await message.reply(f"Выберите тип недвижимости ({district}):", reply_markup=type_kb_ru)
    else:
        await message.reply(f"Mulk turini tanlang ({district}):", reply_markup=type_kb_uz)


async def choose_property_type(message: types.Message):
    property_type = message.text
    filters['type'] = property_type
    if lang == rus and property_type in ['Коммерция', 'Квартира']:
        await message.reply(f"Выберите количкество комнат ({property_type}):", reply_markup=kvart_rooms_kb_ru)
    elif lang == uzb and property_type in ['Tijorat binosi', 'Xonadon']:
        await message.reply(f"Xonalar sonini tanglang ({property_type}):", reply_markup=kvart_rooms_kb_uz)
    elif lang == rus and property_type == 'Дом':
        await message.reply(f"Выберите площадь дома ({property_type}):", reply_markup=dom_type_kb_ru)
    else:
        await message.reply(f"Uy maidonini tanglang ({property_type}):", reply_markup=dom_type_kb_uz)

async def choose_price_room(message: types.Message):
    rooms= message.text
    filters['rooms'] = rooms
    if lang == rus and filters['category'] == 'Аренда':
        await message.reply(f"Выберите цену ({rooms}):", reply_markup=price_aren_kb_ru)
    elif lang == uzb and filters['category'] == 'Ijara':
        await message.reply(f"Narxni tanlang ({rooms}):", reply_markup=price_aren_kb_uz)
    elif lang == rus and filters['category'] == 'Продажа':
        await message.reply(f"Выберите цену ({rooms}):", reply_markup=price_buy_kb_ru)
    else:
        await message.reply(f"Narxni tanlang ({rooms}):", reply_markup=price_buy_kb_uz)

async def choose_price_house(message: types.Message):
    area= message.text
    filters['area'] = area
    if lang == rus and filters['category'] == 'Аренда':
        await message.reply(f"Выберите цену ({area}):", reply_markup=price_aren_kb_ru)
    elif lang == uzb and filters['category'] == 'Ijara':
        await message.reply(f"Narxni tanlang ({area}):", reply_markup=price_aren_kb_uz)
    elif lang == rus and filters['category'] == 'Продажа':
        await message.reply(f"Выберите цену ({area}):", reply_markup=price_buy_kb_ru)
    else:
        await message.reply(f"Narxni tanlang ({area}):", reply_markup=price_buy_kb_uz)

async def search_handler(message: types.Message):
    filters['price'] = message.text
    await message.reply(f"Search for: {filters}")
 
    


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start', 'help'])
    dp.register_message_handler(start, Text(contains='⚙️'))
    dp.register_message_handler(choose_language, Text(equals=rus) | Text(equals=uzb))
    dp.register_message_handler(choose_category, 
                                Text(equals='Аренда') | Text(equals='Продажа') | 
                                Text('Sotuv') | Text('Ijara'))

    dp.register_message_handler(choose_district, lambda message: message.text in list(districts.values())+
                                  list(districts.keys()))
    dp.register_message_handler(choose_property_type, 
                                Text('Квартира') | Text('Коммерция') | 
                                Text('Дом') | Text('Xonadon') | Text('Tijorat binosi') | Text('Hovli'))    

    dp.register_message_handler(choose_price_room, lambda message: message.text in '12345678910')
    dp.register_message_handler(choose_price_house, lambda message: message.text in cotx_list)
    
    dp.register_message_handler(search_handler, lambda message: message.text in price_rent_list)
    dp.register_message_handler(search_handler, lambda message: message.text in price_buy_list)
    dp.register_message_handler(choose_language, Text(contains='🔙'))