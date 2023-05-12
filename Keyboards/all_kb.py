from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

districts = {
    'Mirobod': 'Мирабад',
    'Yakkasaroy': 'Яккасарай',
    'Shayhontohur': 'Шайхантахур',
    'Mirzo Ulug\'bek': 'Мирзо Улугбек',
    'Yashnobod': 'Яшнобод',
    'Yunusobod': 'Юнусабад',
    'Chilonzor': 'Чиланзар',
    'Uchtepa': 'Учтепа',
    'Olmazor': 'Алмазар',
    'Sergeli': 'Сергели',
    'Bektemir': 'Бектемир',
    'Toshkent vil.': 'Тошобл',
}

translator = {
    'Sotuv': 'Продажа',
    'Ijara': 'Аренда',
    'Sale': 'Продажа',
    'Rent': 'Аренда',
    'Xonadon': 'Квартира',
    'Hovli': 'Дом',
    'Tijorat binosi': 'Коммерция',
    'Yangi turar joy': 'Новостройка',
    'Apartment': 'Квартира',
    'House': 'Дом',
    'Commerce': 'Коммерция',
    'New building': 'Новостройка',
    'price_rent_list': {
        '1.000$ - 2.000$': [1_000, 2_000],
        '2.001$ - 3.000$': [2_001, 3_000],
        '3.001$ - 4.000$': [3_001, 4_000],
        '4.001$ - 5.000$': [4_001, 5_000],
        '5.001$ - 6.000$': [5_001, 6_000],
        '6.001$ - 7.000$': [6_001, 7_000],
        '7.001$ - 8.000$': [7_001, 8_000],
        '8.001$ - 9.000$': [8_001, 9_000],
        '9.001$ - 10.000$': [9_001, 10_000],
        '10.001$ +': [10_001, 1_000_000_000_000],
    },
    'price_buy_list': {
        '50.000$ - 70.000$': [50_000, 70_000],
        '70.001$ - 90.000$': [70_001, 90_000],
        '90.001$ - 110.000$': [90_001, 110_000],
        '110.001$ - 150.000$': [110_001, 150_000],
        '150.001$ - 170.000$': [150_001, 170_000],
        '170.001$ - 190.000$': [170_001, 190_000],
        '190.001$ - 210.000$': [190_001, 210_000],
        '210.001$ - 250.000$': [210_001, 250_000],
        '250.001$ +': [250_001, 1_000_000_000_000]
    }
}

back_uz = KeyboardButton('🔙 Ortga')
back_ru = KeyboardButton('🔙 Назад')
back_eng = KeyboardButton('🔙 Back')
back_menu_ru = KeyboardButton('🔄 Менять категорию')
back_menu_uz = KeyboardButton('🔄 Kategoriyani o\'zgartirish')
back_menu_en = KeyboardButton('🔄 Change category')

langs_kb = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
ru = KeyboardButton('🇷🇺 Русский')
uz = KeyboardButton('🇺🇿 O\'zbekcha')
en = KeyboardButton('🇬🇧 English')
langs_kb.row(ru, en).add(uz)

category_kb_ru = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
category_kb_uz = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
category_kb_en = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
cat1_ru = KeyboardButton('Продажа')
cat2_ru = KeyboardButton('Аренда')
cat1_uz = KeyboardButton('Sotuv')
cat2_uz = KeyboardButton('Ijara')
cat1_en = KeyboardButton('Sale')
cat2_en = KeyboardButton('Rent')

back = KeyboardButton('⚙️ Изменить язык')
category_kb_ru.row(cat2_ru, cat1_ru).add(back)

back = KeyboardButton('⚙️ Tilni o\'zgartirish')
category_kb_uz.row(cat2_uz, cat1_uz).add(back)

back = KeyboardButton('⚙️ Change language')
category_kb_en.row(cat2_en, cat1_en).add(back)

district_kb_ru = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
district_kb_uz = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
district_kb_en = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
for i in districts:
    district_kb_ru.add(districts[i])
    district_kb_uz.add(i)
    district_kb_en.add(i)

district_kb_ru.add(back_menu_ru)
district_kb_uz.add(back_menu_uz)
district_kb_en.add(back_menu_en)

type_kb_ru = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
type_kb_uz = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
type_kb_en = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
itembtn1 = KeyboardButton('Квартира')
itembtn2 = KeyboardButton('Дом')
itembtn3 = KeyboardButton('Коммерция')
itembtn4 = KeyboardButton('Новостройка')
itembtn5 = KeyboardButton('Xonadon')
itembtn6 = KeyboardButton('Hovli')
itembtn7 = KeyboardButton('Tijorat binosi')
itembtn8 = KeyboardButton('Yangi turar joy')
itembtn9 = KeyboardButton('Apartment')
itembtn10 = KeyboardButton('House')
itembtn11 = KeyboardButton('Commerce')
itembtn12 = KeyboardButton('New building')
type_kb_ru.row(itembtn1, itembtn2).row(itembtn3, itembtn4).add(back_ru)
type_kb_uz.row(itembtn5, itembtn6).row(itembtn7, itembtn8).add(back_uz)
type_kb_en.row(itembtn9, itembtn10).row(itembtn11, itembtn12).add(back_eng)

kvart_rooms_kb_ru = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
kvart_rooms_kb_uz = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
kvart_rooms_kb_en = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)

for i in range(1, 11):
    kvart_rooms_kb_ru.insert(str(i))
    kvart_rooms_kb_uz.insert(str(i))
    kvart_rooms_kb_en.insert(str(i))

kvart_rooms_kb_ru.insert(back_ru)
kvart_rooms_kb_uz.insert(back_uz)
kvart_rooms_kb_en.insert(back_eng)

cotx_list = ['1-3', '3-5', '5-7', '7-9', '9+']

dom_type_kb_ru = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
dom_type_kb_uz = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
dom_type_kb_en = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

for i in cotx_list:
    dom_type_kb_ru.insert(i)
    dom_type_kb_uz.insert(i)
    dom_type_kb_en.insert(i)
dom_type_kb_ru.insert(back_ru)
dom_type_kb_uz.insert(back_uz)
dom_type_kb_en.insert(back_eng)

price_aren_kb_ru = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
price_aren_kb_uz = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
price_aren_kb_en = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

for i in translator['price_rent_list']:
    price_aren_kb_ru.insert(i)
    price_aren_kb_uz.insert(i)
    price_aren_kb_en.insert(i)

price_aren_kb_ru.insert(back_ru)
price_aren_kb_uz.insert(back_uz)
price_aren_kb_en.insert(back_eng)

price_buy_kb_ru = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
price_buy_kb_uz = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
price_buy_kb_en = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

for i in translator['price_buy_list']:
    price_buy_kb_ru.insert(i)
    price_buy_kb_uz.insert(i)
    price_buy_kb_en.insert(i)

price_buy_kb_ru.insert(back_ru)
price_buy_kb_uz.insert(back_uz)
price_buy_kb_en.insert(back_eng)

go_back_ru = ReplyKeyboardMarkup(resize_keyboard=True).add(back_ru)
go_back_uz = ReplyKeyboardMarkup(resize_keyboard=True).add(back_uz)
