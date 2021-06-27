import asyncio
from aiogram import Bot, Dispatcher, executor
from aiogram import types as agtypes
from aiogram.types import callback_query
from stafflist import *
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")

OWNER_ID = 521241322

YEP_BUTTON = "Done"
NOPE_BUTTON = "🔔🔔🔔 Надо сделать 🔔🔔🔔"

staffList = StaffList()

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, loop=asyncio.get_event_loop())


@dp.callback_query_handler()
async def button_handler(callback_query: agtypes.CallbackQuery):
    markup = agtypes.InlineKeyboardMarkup()

    if (callback_query.data == "Nope"):
        markup.add(agtypes.InlineKeyboardButton(
            YEP_BUTTON, callback_data="Yep"))
    elif (callback_query.data == "Yep"):
        markup.add(agtypes.InlineKeyboardButton(
            NOPE_BUTTON, callback_data="Nope"))

    await callback_query.message.edit_reply_markup(reply_markup=markup)

    await callback_query.answer()


async def loop():

    while True:
        staffList.update()

        added = staffList.get_added()
        updated = staffList.get_updated()
        deleted = staffList.get_deleted()

        for x in added.items():
            markup = agtypes.InlineKeyboardMarkup()
            markup.add(agtypes.InlineKeyboardButton(
                NOPE_BUTTON, callback_data="Nope"))

            text = \
                f"""
<u><b>❇️ Добавлена запись ❇️</b></u>

<b>ID</b> : {x[0]}
<b>UserID</b> : {x[1].userId}
<b>Username</b> : {x[1].username}
<b>Server</b> : {x[1].server}
<b>Rank</b> : {x[1].rank}

-------------

<b><a href=\"https://hil.su/user/{x[1].username}\">Страница пользователя</a></b>

<b><a href=\"https://f.hil.su/members?username={x[1].username}\">Форум</a></b>
"""
            await bot.send_message(chat_id=OWNER_ID, text=text, parse_mode="HTML", reply_markup=markup)

        for x in updated.items():
            markup = agtypes.InlineKeyboardMarkup()
            markup.add(agtypes.InlineKeyboardButton(
                NOPE_BUTTON, callback_data="Nope"))

            text1 = \
                f"""
<u><b>✴️ Изменена запись ✴️</b></u>

<b>ID</b> : {x[0]}
<b>UserID</b> : {x[1][0].userId if x[1][0].userId == x[1][1].userId else f"<s>{x[1][0].userId}</s> <code>{x[1][1].userId}</code>"}
<b>Username</b> : {x[1][0].username if x[1][0].username == x[1][1].username else f"<s>{x[1][0].username}</s> <code>{x[1][1].username}</code>"}
<b>Server</b> : {x[1][0].server if x[1][0].server == x[1][1].server else f"<s>{x[1][0].server}</s> <code>{x[1][1].server}</code>"}
<b>Rank</b> : {x[1][0].rank if x[1][0].rank == x[1][1].rank else f"<s>{x[1][0].rank}</s> <code>{x[1][1].rank}</code>"}

"""

            if x[1][0].username == x[1][1].username:
                text2 = \
                    f"""
-------------

<b><a href=\"https://hil.su/user/{x[1][0].username}\">Страница пользователя</a></b>

<b><a href=\"https://f.hil.su/members?username={x[1][0].username}\">Форум</a></b>
"""
            else:
                text2 = \
                    f"""
-------------

<b><a href=\"https://hil.su/user/{x[1][0].username}\">Старая Страница пользователя</a>
<a href=\"https://hil.su/user/{x[1][1].username}\">Новая Страница пользователя</a></b>

<b><a href=\"https://f.hil.su/members?username={x[1][0].username}\">Старый Форум</a>
<a href=\"https://f.hil.su/members?username={x[1][1].username}\">Новый Форум</a></b>
"""

            await bot.send_message(chat_id=OWNER_ID, text=text1 + text2, parse_mode="HTML", reply_markup=markup)

        for x in deleted.items():
            markup = agtypes.InlineKeyboardMarkup()
            markup.add(agtypes.InlineKeyboardButton(
                NOPE_BUTTON, callback_data="Nope"))

            text = \
                f"""
<u><b>❌ Удалена запись ❌</b></u>

<b>ID</b> : {x[0]}
<b>UserID</b> : {x[1].userId}
<b>Username</b> : {x[1].username}
<b>Server</b> : {x[1].server}
<b>Rank</b> : {x[1].rank}

-------------

<b><a href=\"https://hil.su/user/{x[1].username}\">Страница пользователя</a></b>

<b><a href=\"https://f.hil.su/members?username={x[1].username}\">Форум</a></b>
"""
            await bot.send_message(chat_id=OWNER_ID, text=text, parse_mode="HTML", reply_markup=markup)

        staffList.save()

        await asyncio.sleep(30)

if __name__ == "__main__":
    dp.loop.create_task(loop())
    executor.start_polling(dp)
