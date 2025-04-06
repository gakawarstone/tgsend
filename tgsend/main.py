import os
import sys
import asyncio
from typing import Tuple
from pathlib import Path

from dotenv import load_dotenv
from aiogram import Bot
from aiogram.types import FSInputFile


ENV_PATH = Path().home() / ".config/tgsend/.env"
load_dotenv(ENV_PATH)


def get_config() -> Tuple[Bot, str]:
    try:
        BOT_TOKEN = os.environ["BOT_TOKEN"]
        CHAT_ID = os.environ["CHAT_ID"]
        return (Bot(BOT_TOKEN), CHAT_ID)
    except KeyError:
        print("please run init first")
        exit(1)


async def async_main():
    if len(sys.argv) == 1:
        print("or provide file as an argument")
        return 1
    if sys.argv[1] == "init":
        open(ENV_PATH, "w").write("BOT_TOKEN=" + input("BOT_TOKEN=") + "\n")
        open(ENV_PATH, "a").write("CHAT_ID=" + input("CHAT_ID=") + "\n")
        return

    bot, chat_id = get_config()

    match sys.argv[1]:
        case "-m":
            text = " ".join(sys.argv[2:])
            await bot.send_message(chat_id, text)
        case _:
            bot, chat_id = get_config()
            for path in sys.argv[1:]:
                file = FSInputFile(os.getcwd() + "/" + path)
                await bot.send_document(chat_id, file)

    await bot.session.close()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
