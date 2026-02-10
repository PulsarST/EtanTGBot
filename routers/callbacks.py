from aiogram.dispatcher.router import Router
from aiogram.filters import CommandStart
from aiogram.filters.command import Command
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start_command(meesage: Message):
    """function to procces start command and send hello to user"""

    if meesage.from_user is None:
        return

    user_first_name = meesage.from_user.first_name
    await meesage.answer(f"Hi, {user_first_name} !")


@router.message(Command("review"))
async def send_review(message: Message):
    await message.answer("i got your review !")
