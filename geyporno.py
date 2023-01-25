from data import monday, tuesday, wednesday, thursday, friday, saturday


async def send_message_monday(bot):
    await bot.send_message(chat_id=863797568, text=monday,parse_mode="HTML")


async def send_message_tuesday(bot):
    await bot.send_message(chat_id=863797568, text=tuesday, parse_mode="HTML")


async def send_message_wednesday(bot):
    await bot.send_message(chat_id=863797568, text=wednesday,parse_mode="HTML")


async def send_message_thursday(bot):
    await bot.send_message(chat_id=863797568, text=thursday,parse_mode="HTML")


async def send_message_friday(bot):
    await bot.send_message(chat_id=863797568, text=friday,parse_mode="HTML")


async def send_message_saturday(bot):
    await bot.send_message(chat_id=863797568, text=saturday,parse_mode="HTML")
