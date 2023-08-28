import os
import sys
import asyncio

from dotenv import load_dotenv
from aiogram import Bot
from aiogram.types import FSInputFile


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(ROOT_DIR + '/.env')

BOT_TOKEN = os.environ['BOT_TOKEN']
CHAT_ID = os.environ['CHAT_ID']

bot = Bot(BOT_TOKEN)


async def main():
    match sys.argv[1]:
        case '-m':
            text = ' '.join(sys.argv[2:])
            await bot.send_message(CHAT_ID, text)
        case _:
            for path in sys.argv[1:]:
                file = FSInputFile(os.getcwd() + '/' + path)
                await bot.send_document(CHAT_ID, file)
    await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
