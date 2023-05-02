from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

districts = {
    'Бектемирский район' : 'Bektemir tumani', 
    'Чиланзарский район': 'Chilonzor tumani', 
    'Мирабадский район' :'Mirobod tumani', 
    'Мирзо Улугбекский район' : 'Mirzo Ulug\'bek tumani', 
    'Алмазарский район' : 'Olmazor tumani', 
    'Сергелийский район' : 'Sergeli tumani', 
    'Шайхонтохурский район' : 'Shayhontohur tumani', 
    'Учтепинский район' : 'Uchtepa tumani', 
    'Яккасарайский район' : 'Yakkasaroy tumani', 
    'Яшнаабадский район' : 'Yashnaobod tumani', 
    'Юнусабадский район' : 'Yunusobod tumani', 
    'Ташкентская обл.' : 'Toshkent vil.'
}

back_uz = KeyboardButton('🔙 Ortga')
back_ru = KeyboardButton('🔙 Назад')

langs_kb = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
ru = KeyboardButton('🇷🇺 Русский')
uz = KeyboardButton('🇺🇿 O\'zbekcha')
langs_kb.add(ru, uz)


category_kb_ru = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
category_kb_uz = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
cat1_ru = KeyboardButton('Продажа')
cat2_ru = KeyboardButton('Аренда')
cat1_uz = KeyboardButton('Sotuv')
cat2_uz = KeyboardButton('Ijara')

back = KeyboardButton('⚙️ Изменить язык')
category_kb_ru.row(cat2_ru, cat1_ru).add(back)

back = KeyboardButton('⚙️ Tilni o\'zgartirish')
category_kb_uz.row(cat2_uz, cat1_uz).add(back)


district_kb_ru = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
district_kb_uz = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
for i in districts:
    district_kb_ru.add(i)
    district_kb_uz.add(districts[i])

district_kb_ru.add(back_ru)
district_kb_uz.add(back_uz)

type_kb_ru = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
type_kb_uz = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
itembtn1 = KeyboardButton('Квартира')
itembtn2 = KeyboardButton('Дом')
itembtn3 = KeyboardButton('Коммерция')
itembtn4 = KeyboardButton('Новостройка')
itembtn5 = KeyboardButton('Xonadon')
itembtn6 = KeyboardButton('Hovli')
itembtn7 = KeyboardButton('Tijorat binosi')
itembtn8 = KeyboardButton('Yangi turar joy')
type_kb_ru.row(itembtn1, itembtn2).row(itembtn3, itembtn4).add(back_ru)
type_kb_uz.row(itembtn5, itembtn6).row(itembtn7, itembtn8).add(back_uz)


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


price_rent_list = ['1000 $ - 2000 $','2001 $ - 3000 $ ', '3001 $ - 4000 $', '4001 $ - 5000 $', '5001 $ +']

price_aren_kb_ru = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
price_aren_kb_uz = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

for i in price_rent_list:
    price_aren_kb_ru.insert(i)
    price_aren_kb_uz.insert(i)

price_aren_kb_ru.insert(back_ru)
price_aren_kb_uz.insert(back_uz)


price_buy_list = ['50000$ - 70000 $','70001 $ - 90000 $', '90001 $ - 110000 $', '110001 $ - 150000 $', '150001 $ +']

price_buy_kb_ru = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
price_buy_kb_uz = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

for i in price_buy_list:
    price_buy_kb_ru.insert(i)
    price_buy_kb_uz.insert(i)

price_buy_kb_ru.insert(back_ru)
price_buy_kb_uz.insert(back_uz)
