import asyncio
import app.keyboards as kb

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.fsm.context import FSMContext


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    text = (
        "Привет! Это минимальный шаблон бота на <b>aiogram v3</b>.\n"
        "• /start — перезапуск\n"
        "• /help — справка\n\n"
        "Попробуй кнопки ниже 👇"
    )
    await message.answer(text)