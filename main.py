from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN
from animal import get_fox_urls, get_dog_urls, get_cat_urls

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я животно бот. Введите /help что бы посмотреть команды.")


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply(
        "Если вы напишите /cat вам выведутся фото с кошками, /dog вам ведутся фото с собаками, /fox вам ведутся фото с лисами, Если вы напишите /cat 10 вам выведутся фото с кошками, /dog 10 вам ведутся фото с собаками, /fox 10 вам ведутся фото с лисами.")


def get_int_arg(message: types.Message):
    args = message.get_args()
    args = args.split()
    count = None
    if len(args) == 1:
        count = args[0]
        if count.isdigit():
            count = int(count)
    return count


@dp.message_handler(commands=['cat'])
async def send_cat_photo(message: types.Message):
    count = get_int_arg(message)
    if count is None:
        count = 1
    urls = await get_cat_urls(count)
    for image_url in urls:
        await bot.send_photo(message.chat.id, photo=image_url)


@dp.message_handler(commands=['dog'])
async def send_dog_photo(message: types.Message):
    count = get_int_arg(message)
    if count is None:
        count = 1
    urls = await get_dog_urls(count)
    for image_url in urls:
        await bot.send_photo(message.chat.id, photo=image_url)


@dp.message_handler(commands=['fox'])
async def send_fox_photo(message: types.Message):
    count = get_int_arg(message)
    if count is None:
        count = 1
    urls = await get_fox_urls(count)
    for image_url in urls:
        await bot.send_photo(message.chat.id, photo=image_url)


if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp)
