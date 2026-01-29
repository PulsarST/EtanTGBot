import asyncio
import os

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
assert (
    bot_token is not None
)  # check bot_token, actually it need for pyright to stop warning

bot = Bot(bot_token)
dp = Dispatcher()


@dp.message(F.text == "/start")
async def start(message: Message):
    """function to procces command start and send hello to user"""

    if message.from_user is None:
        return

    user_first_name = message.from_user.first_name
    await message.answer(f"hello, {user_first_name}")


async def main() -> None:
    """main function, it starts polling and configures general projects components"""

    """
    it needs to off answeting on each /start command from user,
    bacause user can send a lot of /start command and to reduce it we delete webhook which
    responsible for it
    """
    await bot.delete_webhook(drop_pending_updates=True)

    "starts polling"
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
