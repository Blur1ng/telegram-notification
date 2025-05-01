import os
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery, InlineKeyboardMarkup
from aiogram.filters import Command
from functools import wraps

from app.notification.sqlalchemy_classes import GetData, SetData, AddData

from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TOKEN")

dp = Dispatcher()

def vipusers_only(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        message = kwargs.get("message")
        if not message and args:
            for arg in args:
                if isinstance(arg, (Message, CallbackQuery)):
                    message = arg
                    break

        if not message:
            return await func(*args, **kwargs)

        username = message.from_user.username
        VIPusers = await GetData.get_all_VIPUsers()
        vip_usernames = [user.name for user in VIPusers]

        if username not in vip_usernames:
            await message.answer("🚫 Not VIP User")
            return

        return await func(*args, **kwargs)
    return wrapper

@dp.message(Command("getvipusers"))
@vipusers_only
async def send_message(message: Message) -> None:
    VIPusers = await GetData.get_all_VIPUsers()
    result = " ".join([user.name for user in VIPusers])
    if VIPusers:
        await message.answer(result)
    else:
        await message.answer("No users found")

@dp.message(Command("not"))
@vipusers_only
async def start_command(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🔌 Вкл", callback_data="noton"),
                InlineKeyboardButton(text="🔌 Выкл", callback_data="notoff"),
            ]
        ]
    )
    await message.answer("Выберите действие:", reply_markup=keyboard)

@dp.callback_query(F.data == "noton")
async def notification_on(callback: CallbackQuery):
    username = callback.from_user.username
    user = await GetData.get_VIPUser(username)
    await SetData.on_notification(user)
    await callback.answer("Включено ✅", show_alert=True)
    await callback.message.edit_text("Текущее состояние: 🔛 ВКЛ")

@dp.callback_query(F.data == "notoff")
async def on_power_off(callback: CallbackQuery):
    username = callback.from_user.username
    user = await GetData.get_VIPUser(username)
    await SetData.off_notification(user)
    await callback.answer("Выключено ❌", show_alert=True)
    await callback.message.edit_text("Текущее состояние: 🔴 ВЫКЛ")

@dp.message(Command("addvipuser"))
@vipusers_only
async def add_vip_user(message: Message) -> None:
    username = message.from_user.username
    await AddData.add_VIPUser(username)

async def start_telegram_app() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)
