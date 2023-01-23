from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio
import aioschedule

TOKEN_API = '5974312085:AAFXoviRvo7w6FRUg9mdkMGN7E19dJzhd0I'

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

ckb = InlineKeyboardMarkup(row_width=2)
ckb.add(InlineKeyboardButton('Назад👨🏼‍🦽',
                             callback_data='Back'))

kb = ReplyKeyboardMarkup()
kb.add(KeyboardButton('Помоги мне😓'))
kb.add(KeyboardButton('Зачем я нужен🤗'))
kb.add(KeyboardButton('Школа🥶'))

HELP_COMMAND = """
/help - список команд
/start - начать работу с ботом
/description - что я умею
/School schedule - школьное расписание"""


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
        text=f'<em><b>1)👽Разговоры о важном👽\n2)🤝Физ-Ра🤝\n3)💋История💋\n4)☠️Русский Язык☠️\n5)💩Математика💩\n'
             f'6)🥴Страноведение🥴\n7)💋Право💋</b></em>',
        parse_mode="HTML",
        reply_markup=ckb)
    await callback.message.delete()


@dp.callback_query_handler(lambda callback_query: callback_query.data == 'Tuesday')
async def M(callback: types.CallbackQuery):
    await callback.message.answer(
        text=f'<em><b>1)💋Общество💋\n2)💩Математика💩\n3)👾Биология👾\n4)☠️Л️итература☠️\n5)🥴Англ.Яз.🥴\n'
             f'6)😵‍💫Физика😵‍💫</b></em>',
        parse_mode="HTML",
        reply_markup=ckb)
    await callback.message.delete()


@dp.callback_query_handler(lambda callback_query: callback_query.data == 'Wednesday')
async def M(callback: types.CallbackQuery):
    await callback.message.answer(
        text=f'<em><b>1)🤤Химия🤤\n2)🤝Физ-Ра🤝\n3)☠️Литература☠️\n4)☠️Русский Язык☠️\n5)😵‍💫Астрономия😵‍💫\n'
             f'6)💩Математика💩</b></em>',
        parse_mode="HTML",
        reply_markup=ckb)
    await callback.message.delete()


@dp.callback_query_handler(lambda callback_query: callback_query.data == 'Thursday')
async def M(callback: types.CallbackQuery):
    await callback.message.answer(
        text=f'<em><b>1)💋Право💋\n2)🥴Англ.Яз.🥴\n3)💩Математика💩\n4)🤪География🤪\n5)💋История💋\n'
             f'6)💩Практикум по Математике💩</b></em>',
        parse_mode="HTML",
        reply_markup=ckb)
    await callback.message.delete()


@dp.callback_query_handler(lambda callback_query: callback_query.data == 'Friday')
async def M(callback: types.CallbackQuery):
    await callback.message.answer(
        text=f'<em><b>1)🤝Физ-Ра🤝\n2)😵‍💫Физика😵‍💫\n3)☠️Русский Язык☠️\n4)☠️Литература☠️\n5)💩Математика💩\n'
             f'6)💋Общество💋\n🏃🏼‍♂️️Функц.Гр.🏃🏼‍♂️</b></em>',
        parse_mode="HTML",
        reply_markup=ckb)
    await callback.message.delete()


@dp.callback_query_handler(lambda callback_query: callback_query.data == 'Saturday')
async def M(callback: types.CallbackQuery):
    await callback.message.answer(
        text=f'<em><b>1)🥴Англ.Яз.🥴\n2)💅🏼Информатика💅🏼\n3)💩Математика💩\n4)💆🏼‍♂️Кубановедение💆🏼‍♂️\n5)🎩ОБЖ🎩\n'
             f'6)🦧Практикум по Русскому🦧</b></em>',
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


@dp.message_handler()
async def Monday_(users):
    for user in set(users):
        await bot.send_message(chat_id=user, text="Хей🖖 не забудь выбрать свой ужин сегодня")


@dp.message_handler()
async def Tuesday_(users):
    for user in set(users):
        await bot.send_message(chat_id=user, text="Хей🖖 не забудь выбрать свой ужин сегодня")


@dp.message_handler()
async def Wednesday_(users):
    for user in set(users):
        await bot.send_message(chat_id=user, text="Хей🖖 не забудь выбрать свой ужин сегодня")


@dp.message_handler()
async def Thursday_(users):
    for user in set(users):
        await bot.send_message(chat_id=user, text="Хей🖖 не забудь выбрать свой ужин сегодня")


@dp.message_handler()
async def Friday(users):
    for user in set(users):
        await bot.send_message(chat_id=user, text="Хей🖖 не забудь выбрать свой ужин сегодня")


@dp.message_handler()
async def Saturday_(users):
    for user in set(users):
        await bot.send_message(chat_id=user, text="Хей🖖 не забудь выбрать свой ужин сегодня")


async def scheduler():
    aioschedule.every().day.at("06:40").do(choose_your_dinner)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

async def on_startup(dp):
    asyncio.create_task(scheduler())



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
