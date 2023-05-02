from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

districts = ['Яккасарай', 'Мирабад', 'Шайхантахур',
             'Мирзо-Улугбек', 'Юнусабад', 'Чиланзар',
             'Яшнабад', 'Сергели', 'Бектемир', 'Алмазар', 'Таш. область']

back_uz = KeyboardButton('🔙 Ортга')
back_ru = KeyboardButton('🔙 Назад')

langs_kb = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
ru = KeyboardButton('🇷🇺 Русский')
uz = KeyboardButton('🇺🇿 Ўзбекча')
langs_kb.add(ru, uz)


category_kb_ru = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
category_kb_uz = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
cat1_ru = KeyboardButton('Продажа')
cat2_ru = KeyboardButton('Аренда')
cat1_uz = KeyboardButton('Сотув')
cat2_uz = KeyboardButton('Ижара')

back = KeyboardButton('⚙️ Изменить язык')
category_kb_ru.row(cat1_ru, cat2_ru).add(back)

back = KeyboardButton('⚙️ Тилни ўзгартириш')
category_kb_uz.row(cat1_uz, cat2_uz).add(back)


district_kb_ru = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
district_kb_uz = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
for i in districts:
    district_kb_ru.add(i)
    district_kb_uz.add(i)

district_kb_ru.add(back_ru)
district_kb_uz.add(back_uz)

type_kb_ru = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
type_kb_uz = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
itembtn1 = KeyboardButton('Квартира')
itembtn2 = KeyboardButton('Дом')
itembtn3 = KeyboardButton('Коммерция')
itembtn4 = KeyboardButton('Хонадон')
type_kb_ru.row(itembtn1, itembtn2, itembtn3).add(back_ru)
type_kb_uz.row(itembtn1, itembtn4, itembtn3).add(back_uz)


kvart_rooms_kb_ru = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
kvart_rooms_kb_uz = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)

for i in range(1,11):
    kvart_rooms_kb_ru.insert(str(i))
    kvart_rooms_kb_uz.insert(str(i))
    
kvart_rooms_kb_ru.insert(back_ru)
kvart_rooms_kb_uz.insert(back_uz)

cotx_list = ['1-3', '3-5', '5-7', '7-9', '9+'] 

dom_type_kb_ru = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
dom_type_kb_uz = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

for i in cotx_list:
    dom_type_kb_ru.insert(i)
    dom_type_kb_uz.insert(i)
dom_type_kb_ru.insert(back_ru)
dom_type_kb_uz.insert(back_uz)


price_rent_list = ['1000дол-2000дол','2000дол-3000дол', '3000дол-4000дол', '4000дол-5000дол', '5000дол+']

price_aren_kb_ru = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
price_aren_kb_uz = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

for i in price_rent_list:
    price_aren_kb_ru.insert(i)
    price_aren_kb_uz.insert(i)

price_aren_kb_ru.insert(back_ru)
price_aren_kb_uz.insert(back_uz)


price_buy_list = ['50000дол-70000дол','70000дол-90000дол', '90000дол-110000дол', '110000дол-150000дол', '150000дол+']

price_buy_kb_ru = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
price_buy_kb_uz = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

for i in price_buy_list:
    price_buy_kb_ru.insert(i)
    price_buy_kb_uz.insert(i)

price_buy_kb_ru.insert(back_ru)
price_buy_kb_uz.insert(back_uz)