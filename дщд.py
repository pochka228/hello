import requests
import random
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = '5846038926:AAFncUzXEPtnOb5pjPa8u97d4GYZs320obg'

bot = Bot(token='5846038926:AAFncUzXEPtnOb5pjPa8u97d4GYZs320obg')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я животно бот. Чем я могу тебе помочь?")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("Если вы напишите /cat вам выведутся фото с кошками, /dog вам ведутся фото с собаками, /fox вам ведутся фото с лисами.")

async def send_cat_photo(message: types.Message):
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    data = response.json()@dp.message_handler(commands=['cat'])

@dp.message_handler(commands=['cat'])
async def send_cat_photo(message: types.Message):
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    data = response.json()
    image_url = data[0]['url']
    await bot.send_photo(message.chat.id, photo=image_url)

@dp.message_handler(commands=['dog'])
async def send_cat_photo(message: types.Message):
    response = requests.get('https://api.thedogapi.com/v1/images/search')
    data = response.json()
    image_url = data[0]['url']
    await bot.send_photo(message.chat.id, photo=image_url)

@dp.message_handler(commands=['fox'])
async def send_fox_photo(message: types.Message):
    response = requests.get('https://randomfox.ca/floof/')
    data = response.json()
    image_url = data['image']
    await bot.send_photo(message.chat.id, photo=image_url)


@dp.message_handler(commands=['fish'])
async def send_fish_photo(message: types.Message):
    response = requests.get('https://picsum.photos/200/300')
    data = response.json()
    image_url = data[0]['image']
    await bot.send_photo(message.chat.id, photo_image_url)

from aiogram import executor
executor.start_polling(dp)


