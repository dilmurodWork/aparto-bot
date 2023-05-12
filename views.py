from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from Keyboards.all_kb import *
from settings import bot, phone, chanel_id
from filter_posts import get_filtred_msgs_id
from aiogram.dispatcher.filters.state import State, StatesGroup
from ChannelMessages import main


class Form(StatesGroup):
    category = State()
    district = State()
    type = State()
    area = State()
    price = State()
    search_data = State()


rus = '🇷🇺 Русский'
uzb = '🇺🇿 O\'zbekcha'
eng = '🇬🇧 English'
filters = {}


async def start(message: types.Message, state: FSMContext):
    text = 'Xush kelibsiz, tilni tanlang.\nДобро пожаловать выберите язык.\nWelcome choose language.'
    await state.finish()
    try:
        await bot.send_message(message.from_user.id, text, reply_markup=langs_kb)
        await message.delete()
        await Form.category.set()
    except:
        await message.reply('Переход в ЛС, напишите ему \ Shaxsiy habarlarga yozing \ Go to PM, write to him:\nhttps://t.me/dnm_test_bot')


async def choose_category(message: types.Message, state: FSMContext):
    await Form.category.set()

    async with state.proxy() as data:
        if '🔄' not in message.text:
            data['lang'] = message.text

        if data['lang'] == rus:
            await message.reply(f"Выберите категорию ({data['lang']}):", reply_markup=category_kb_ru)
        elif data['lang'] == eng:
            await message.reply(f"Select a category ({data['lang']}):", reply_markup=category_kb_en)
        else:
            await message.reply(f"Kategoriyani tanlang ({data['lang']}):", reply_markup=category_kb_uz)

        await Form.next()


async def choose_district(message: types.Message, state: FSMContext):
    await Form.district.set()

    async with state.proxy() as data:
        try:
            if '🔙' not in message.text:
                data['category'] = translator[message.text]
        except KeyError:
            if '🔙' not in message.text:
                data['category'] = message.text

        if data['lang'] == rus:
            await message.reply(f"Выберите район ({data['category']}):", reply_markup=district_kb_ru)
        elif data['lang'] == eng:
            await message.reply(f"Select a district ({data['category']}):", reply_markup=district_kb_en)
        else:
            await message.reply(f"Tumanni tanlang ({data['category']}):", reply_markup=district_kb_uz)

        await Form.next()


async def choose_type(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data['district'] = districts[message.text]
        except KeyError:
            data['district'] = message.text

        if data['lang'] == rus:
            await message.reply(f"Выберите тип недвижимости ({data['district']}):", reply_markup=type_kb_ru)
        elif data['lang'] == eng:
            await message.reply(f"Choose a type ({data['district']}):", reply_markup=type_kb_en)
        else:
            await message.reply(f"Mulk turini tanlang ({data['district']}):", reply_markup=type_kb_uz)

    await Form.next()


async def choose_area(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data['type'] = translator[message.text]
        except KeyError:
            data['type'] = message.text

        if data['type'] in ['Коммерция', 'Квартира', 'Новостройка']:
            if data['lang'] == rus:
                await message.reply(f"Выберите количкество комнат ({data['type']}):", reply_markup=kvart_rooms_kb_ru)
            elif data['lang'] == uzb:
                await message.reply(f"Xonalar sonini tanglang ({data['type']}):", reply_markup=kvart_rooms_kb_uz)
            else:
                await message.reply(f"Choose number of rooms  ({data['type']}):", reply_markup=kvart_rooms_kb_en)

        elif data['type'] == 'Дом':
            if data['lang'] == rus:
                await message.reply(f"Выберите площадь дома ({data['type']}):", reply_markup=dom_type_kb_ru)
            elif data['lang'] == eng:
                await message.reply(f"Select the area ({data['type']}):", reply_markup=dom_type_kb_en)
            else:
                await message.reply(f"Uy maidonini tanglang ({data['type']}):", reply_markup=dom_type_kb_uz)

    await Form.next()


async def choose_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data['area'] = translator[message.text]
        except KeyError:
            data['area'] = message.text

        if data['category'] == 'Аренда':
            if data['lang'] == rus:
                await message.reply(f"Выберите цену ({data['area']}):", reply_markup=price_aren_kb_ru)
            elif data['lang'] == uzb:
                await message.reply(f"Narxni tanlang ({data['area']}):", reply_markup=price_aren_kb_uz)
            else:
                await message.reply(f"Choose a price ({data['area']}):", reply_markup=price_aren_kb_en)

        elif data['category'] == 'Продажа':
            if data['lang'] == rus:
                await message.reply(f"Выберите цену ({data['area']}):", reply_markup=price_buy_kb_ru)
            elif data['lang'] == uzb:
                await message.reply(f"Narxni tanlang ({data['area']}):", reply_markup=price_buy_kb_uz)
            else:
                await message.reply(f"Choose a price ({data['area']}):", reply_markup=price_buy_kb_en)

        await Form.next()


async def search_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data['price'] = translator['price_buy_list'][message.text]
        except KeyError:
            data['price'] = translator['price_rent_list'][message.text]

    messages_id = get_filtred_msgs_id(dict(data))
    print(messages_id)
    for msg in messages_id:
        await bot.forward_message(message.from_user.id, chanel_id, message_id=msg)


def register_handlers_view(dp: Dispatcher):
    dp.register_message_handler(start, commands='start', state='*')
    dp.register_message_handler(start, Text(contains='⚙️'), state='*')
    dp.register_message_handler(choose_category, state=Form.category)

    dp.register_message_handler(choose_district, Text('Аренда') | Text('Продажа') |
                                Text('Sotuv') | Text('Ijara') | Text('Sale') | Text('Rent'), state=Form.district)

    dp.register_message_handler(choose_type,
                                lambda message: message.text in list(districts.values()) + list(districts.keys()),
                                state=Form.type)

    dp.register_message_handler(choose_area,
                                Text('Квартира') | Text('Коммерция') | Text('Новостройка') |
                                Text('Дом') | Text('Xonadon') | Text('Tijorat binosi') | Text('Hovli') |
                                Text('Yangi turar joy') | Text('Apartment') |
                                Text('House') | Text('Commerce') | Text('New building'),
                                state=Form.area)

    dp.register_message_handler(choose_price,
                                lambda message: message.text in '12345678910' or message.text in cotx_list,
                                state=Form.price)

    dp.register_message_handler(search_handler, lambda message: message.text in translator['price_rent_list'],
                                state=Form.search_data)
    dp.register_message_handler(search_handler, lambda message: message.text in translator['price_buy_list'],
                                state=Form.search_data)
    dp.register_message_handler(choose_district, Text(contains='🔙'), state='*')
    dp.register_message_handler(choose_category, Text(contains='🔄'), state='*')
