from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Стоимость'),
            KeyboardButton(text='О нас')
        ]
    ],
    resize_keyboard=True
) 

catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Средняя игра ", callback_data="medium")],
        [InlineKeyboardButton(text="Большая игра", callback_data="big")],
        [InlineKeyboardButton(text="Очень большая игра", callback_data="mega")],
        [InlineKeyboardButton(text="Другая игра", callback_data="other")],
    ]
)

buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Купить!", url="https://t.me/loolohka_bot")],
    ]
)