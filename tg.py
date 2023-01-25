import datetime
import sqlite3
from hui import AlreadySubError
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from geyporno import send_message_monday, send_message_tuesday, send_message_wednesday, send_message_thursday, send_message_friday, send_message_saturday
from data import monday, tuesday, wednesday, thursday, friday, saturday

TOKEN_API = '5974312085:AAFXoviRvo7w6FRUg9mdkMGN7E19dJzhd0I'

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

# Connect to the SQLite database
conn = sqlite3.connect('subscribers.db')
c = conn.cursor()

# Create the subscribers table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS subscribers (chat_id INTEGER PRIMARY KEY)''')

ckb = InlineKeyboardMarkup(row_width=2)
ckb.add(InlineKeyboardButton('Назад👨🏼‍🦽', callback_data='Back'))

kb = ReplyKeyboardMarkup()
kb.add(KeyboardButton('🤗Зачем я нужен🤗'))
kb.add(KeyboardButton('🥶Школа🥶'))
kb.add(KeyboardButton('🧠Подписка на рассылку🧠'))


@dp.message_handler(text= '🧠Подписка на рассылку🧠')
async def subscribe(message: types.Message):
    try:
        chat_id = message.from_user.id
        c.execute("INSERT INTO subscribers (chat_id) VALUES (?)", (chat_id,))
        conn.commit()
        await message.reply("👍🏼ВЫ СДЕЛАЛИ АХУЕННО👍🏼")
    except sqlite3.IntegrityError:
        await message.reply('НЕ КЛИКАЙ СЮДА БОЛЬШЕ')
        await bot.send_sticker(message.from_user.id,
                                     sticker='CAACAgIAAxkBAAEHa9Vj0F00v0npxjkDAom7ZIQ3EQZ6lgACGhUAAru3aUjlYr57-57PNC0E')


@dp.message_handler(text= '🤗Зачем я нужен🤗')
async def help_command(message: types.Message):
    await message.answer('<em><b>Данный бот будет напоминать вам о вашем школьном рассписание</b></em>',
                         parse_mode="HTML")
    await message.delete()


@dp.message_handler(commands=['start'])
async def help_command(message: types.Message):
    await message.answer(text='<em><b>Добро пожаловать в мой телеграм Бот!</b></em>', parse_mode="HTML",
                         reply_markup=kb)
    await bot.send_sticker(message.from_user.id,
                           sticker="CAACAgIAAxkBAAEHa9lj0F4VT3V4r6xGOAFoT_Jj4GlvygACWBcAAhcbIEiLeUa9nKxvcy0E")
    await message.delete()


@dp.message_handler(text= '🥶Школа🥶')
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


@dp.callback_query_handler(text= 'Monday')
async def M(callback: types.CallbackQuery):
    await callback.message.answer(
        text=monday,
        parse_mode="HTML",
        reply_markup=ckb)
    await callback.message.delete()


@dp.callback_query_handler(text= 'Tuesday')
async def V(callback: types.CallbackQuery):
    await callback.message.answer(
        text=tuesday,
        parse_mode="HTML",
        reply_markup=ckb)
    await callback.message.delete()


@dp.callback_query_handler(text= 'Wednesday')
async def G(callback: types.CallbackQuery):
    await callback.message.answer(
        text=wednesday,
        parse_mode="HTML",
        reply_markup=ckb)
    await callback.message.delete()


@dp.callback_query_handler(text= 'Thursday')
async def D(callback: types.CallbackQuery):
    await callback.message.answer(
        text=thursday,
        parse_mode="HTML",
        reply_markup=ckb)
    await callback.message.delete()


@dp.callback_query_handler(text= 'Friday')
async def E(callback: types.CallbackQuery):
    await callback.message.answer(
        text=friday,
        parse_mode="HTML",
        reply_markup=ckb)
    await callback.message.delete()


@dp.callback_query_handler(text= 'Saturday')
async def L(callback: types.CallbackQuery):
    await callback.message.answer(
        text=saturday,
        parse_mode="HTML",
        reply_markup=ckb)
    await callback.message.delete()


@dp.callback_query_handler(text= 'Back')
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


def schedule_messages():
    cursor = conn.cursor()
    cursor.execute("SELECT chat_id FROM subscribers")
    chat_ids = cursor.fetchall()
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    scheduler.add_job(send_message_monday, trigger='cron', kwargs={'bot' : bot},
                      hour=datetime.datetime.now().hour, minute=datetime.datetime.now().minute + 1)
    scheduler.add_job(send_message_tuesday, trigger='cron', kwargs={'bot' : bot},
                      hour=datetime.datetime.now().hour, minute=datetime.datetime.now().minute + 1)
    scheduler.add_job(send_message_wednesday, trigger='cron', kwargs={'bot' : bot},
                      hour=datetime.datetime.now().hour, minute=datetime.datetime.now().minute + 1)
    scheduler.add_job(send_message_thursday, trigger='cron', kwargs={'bot' : bot},
                      hour=datetime.datetime.now().hour, minute=datetime.datetime.now().minute + 1)
    scheduler.add_job(send_message_friday, trigger='cron', kwargs={'bot' : bot},
                      hour=datetime.datetime.now().hour, minute=datetime.datetime.now().minute + 1)
    scheduler.add_job(send_message_saturday, trigger='cron', kwargs={'bot' : bot},
                      hour=datetime.datetime.now().hour, minute=datetime.datetime.now().minute + 1)
    scheduler.start()#ИЛЮША Я ЗАЕБАЛСЯ ГО ШТУРВАЛОМ ПОДРОЧИМ ДРУГ ДРУГУ


if __name__ == '__main__':
    schedule_messages()
    executor.start_polling(dp, skip_updates=True)
