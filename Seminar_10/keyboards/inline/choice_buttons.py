from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# choice = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text="Старт", callback_data=""),
#             InlineKeyboardButton(text="Стоп", callback_data="cancel")
#         ]
#     ]
# )

choice = InlineKeyboardMarkup(row_width=2)

start_button = InlineKeyboardButton(text="Ответ", callback_data="start")
choice.insert(start_button)

cancel_button = InlineKeyboardButton(text="Мотивация", callback_data="mot")
choice.insert(cancel_button)