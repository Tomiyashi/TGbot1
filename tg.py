import asyncio
from data import monday,tuesday,wednesday,thursday,friday,saturday
import sqlite3
import aioschedule
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from apscheduler.schedulers.background import BackgroundScheduler


TOKEN_API = '5974312085:AAFXoviRvo7w6FRUg9mdkMGN7E19dJzhd0I'

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

# Connect to the SQLite database
conn = sqlite3.connect('subscribers.db')
c = conn.cursor()

# Create the subscribers table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS subscribers (chat_id INTEGER PRIMARY KEY)''')

ckb = InlineKeyboardMarkup(row_width=2)
ckb.add(InlineKeyboardButton('Назад👨🏼‍🦽',callback_data='Back'))

kb = ReplyKeyboardMarkup()
kb.add(KeyboardButton('😓Помоги мне😓'))
kb.add(KeyboardButton('🤗Зачем я нужен🤗'))
kb.add(KeyboardButton('🥶Школа🥶'))
kb.add(KeyboardButton('🧠Подписка на рассылку🧠'))

HELP_COMMAND = """
/help - список команд
/start - начать работу с ботом
/description - что я умею
/School schedule - школьное расписание"""


@dp.message_handler(lambda message:message.text == '🧠Подписка на рассылку🧠')
async def subscribe(message:types.Message):
    chat_id = message.from_user.id
    c.execute("INSERT INTO subscribers (chat_id) VALUES (?)", (chat_id,))
    conn.commit()
    await message.reply("👍🏼ВЫ СДЕЛАЛИ АХУЕННО👍🏼")



@dp.message_handler(lambda message: message.text == 'Зачем я нужен🤗')
async def help_command(message: types.Message):
    await message.answer('<em><b>Данный бот будет напоминать вам о вашем школьном рассписание</b></em>',
                         parse_mode="HTML")
    await message.delete()


@dp.message_handler(lambda message: message.text == 'Помоги мне😓')
async def help_command(message: types.Message):
    await message.answer(text=f'<em><b>Список команд</b></em>\n{HELP_COMMAND}', parse_mode="HTML", )
    await message.delete()


@dp.message_handler(commands=['start'])
async def help_command(message: types.Message):
    await message.answer(text='<em><b>Добро пожаловать в мой телеграм Бот!</b></em>', parse_mode="HTML",
                         reply_markup=kb)
    await bot.send_sticker(message.from_user.id,
                           sticker="CAACAgIAAxkBAAEHZFtjzbsMSGolpDRLUuP7ZWNekwXGlwACJQkAAlZjuEkTBHGd_SLd0S0E")
    await message.delete()


@dp.message_handler(lambda message: message.text == '🧠Подписка на рассылку🧠')
async def help_command(message: types.Message):
    await message.answer('<em><b>Данный бот будет напоминать вам о вашем школьном рассписание</b></em>',
                         parse_mode="HTML")
    await message.delete()

@dp.message_handler(lambda message: message.text == 'Школа🥶')
async def help_command(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=2)
    ikb.add(InlineKeyboardButton('Понедельник🥳',
                                 callback_data='Monday'))
    ikb.add(InlineKeyboardButton('Вторник🫡',
                                 callback_data='Tuesday'))
    ikb.add(InlineKeyboardButton('Среда🫥',
                                 callback_data='Wednesday'))
    ikb.add(InlineKeyboardButton('Четверг🤢',
                                 callback_data='Thursday'))
    ikb.add(InlineKeyboardButton('Пятница🥱',
                                 callback_data='Friday'))
    ikb.add(InlineKeyboardButton('Суббота👺',
                                 callback_data='Saturday'))
    await message.answer('<em><b>Расписание</b></em>', parse_mode="HTML",
                         reply_markup=ikb)
    await message.delete()


@dp.callback_query_handler(lambda callback_query: callback_query.data == 'Monday')
async def M(callback: types.CallbackQuery):
    await callback.message.answer(
        text=monday,
        parse_mode="HTML",
        reply_markup=ckb)
    await callback.message.delete()


@dp.callback_query_handler(lambda callback_query: callback_query.data == 'Tuesday')
async def M(callback: types.CallbackQuery):
    await callback.message.answer(
        text=tuesday,
        parse_mode="HTML",
        reply_markup=ckb)
    await callback.message.delete()


@dp.callback_query_handler(lambda callback_query: callback_query.data == 'Wednesday')
async def M(callback: types.CallbackQuery):
    await callback.message.answer(
        text=wednesday,
        parse_mode="HTML",
        reply_markup=ckb)
    await callback.message.delete()


@dp.callback_query_handler(lambda callback_query: callback_query.data == 'Thursday')
async def M(callback: types.CallbackQuery):
    await callback.message.answer(
        text=thursday,
        parse_mode="HTML",
        reply_markup=ckb)
    await callback.message.delete()


@dp.callback_query_handler(lambda callback_query: callback_query.data == 'Friday')
async def M(callback: types.CallbackQuery):
    await callback.message.answer(
        text=friday,
        parse_mode="HTML",
        reply_markup=ckb)
    await callback.message.delete()


@dp.callback_query_handler(lambda callback_query: callback_query.data == 'Saturday')
async def M(callback: types.CallbackQuery):
    await callback.message.answer(
        text=saturday,
        parse_mode="HTML",
        reply_markup=ckb)
    await callback.message.delete()


@dp.callback_query_handler(lambda callback_query: callback_query.data == 'Back')
async def C(callback: types.CallbackQuery):
    ikb = InlineKeyboardMarkup(row_width=2)
    ikb.add(InlineKeyboardButton('Понедельник🥳',
                                 callback_data='Monday'))
    ikb.add(InlineKeyboardButton('Вторник🫡',
                                 callback_data='Tuesday'))
    ikb.add(InlineKeyboardButton('Среда🫥',
                                 callback_data='Wednesday'))
    ikb.add(InlineKeyboardButton('Четверг🤢',
                                 callback_data='Thursday'))
    ikb.add(InlineKeyboardButton('Пятница🥱',
                                 callback_data='Friday'))
    ikb.add(InlineKeyboardButton('Суббота👺',
                                 callback_data='Saturday'))
    await callback.message.answer('<em><b>Расписание</b></em>', parse_mode="HTML",
                                  reply_markup=ikb)
    await callback.message.delete()


def send_message(chat_id: int, message: str):
    bot.send_message(chat_id=chat_id, text=message)


def schedule_messages():
    cursor = conn.cursor()
    cursor.execute("SELECT chat_id FROM subscribers")
    chat_ids = cursor.fetchall()
    cursor.close()
    conn.close()
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_message, 'interval', (chat_ids, monday),
                          start_date='2023-01-23 06:30:00', end_date='2023-12-31 06:30:00',
                          day_of_week='mon')
    scheduler.add_job(send_message, 'interval', (chat_ids, tuesday),
                          start_date='2023-01-24 06:30:00', end_date='2023-12-31 06:30:00',
                          day_of_week='tue')
    scheduler.add_job(send_message, 'interval', (chat_ids, wednesday),
                          start_date='2023-01-25 06:30:00', end_date='2023-12-31 06:30:00',
                          day_of_week='wed')
    scheduler.add_job(send_message, 'interval', (chat_ids, thursday),
                          start_date='2023-01-26 06:30:00', end_date='2023-12-31 06:30:00',
                          day_of_week='thu')
    scheduler.add_job(send_message, 'interval', (chat_ids, friday),
                          start_date='2023-01-27 06:30:00', end_date='2023-12-31 06:30:00',
                          day_of_week='fri')
    scheduler.add_job(send_message, 'interval', (chat_ids, saturday),
                          start_date='2023-01-28 06:30:00', end_date='2023-12-31 06:30:00',
                          day_of_week='sat')
    scheduler.start()



if __name__ == '__main__':
    schedule_messages()
    executor.start_polling(dp, skip_updates=True)
