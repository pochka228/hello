import aiohttp


async def get_cat_urls(count):
    api_url = f'https://api.thecatapi.com/v1/images/search?limit={count}'
    urls = []

    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as response:
            animal_list = await response.json()
            for animal in animal_list:
                url = animal["url"]
                urls.append(url)
    return urls


async def get_dog_urls(count):
    api_url = f'https://api.thedogapi.com/v1/images/search?limit={count}'
    urls = []

    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as response:
            animal_list = await response.json()
            for animal in animal_list:
                url = animal["url"]
                urls.append(url)
    return urls


async def get_fox_urls(count):
    api_url = 'https://randomfox.ca/floof/'
    urls = []

    async with aiohttp.ClientSession() as session:
        for i in range(count):
            async with session.get(api_url) as response:
                data = await response.json()
                image_url = data['image']
                urls.append(image_url)

    return urls
