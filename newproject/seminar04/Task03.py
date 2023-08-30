# Написать программу, которая считывает список
# из 10 URL-адресов и одновременно загружает данные
# с каждого адреса. После загрузки данных нужно записать их
# в отдельные файлы.
# Используйте асинхронный подход.

import asyncio
import aiohttp
from multiprocessing import Process
import threading
import requests
import time

urls = [
    'https://www.google.ru/',
    'https://gb.ru/',
    'https://ya.ru/',
    'https://www.python.org/',
    'https://habr.com/ru/all/',
    'https://dzen.ru/',
    'https://rambler.ru/',
    'https://gq.ru/',
    'https://vc.ru/',
    ]

async def get_urls(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            filename = 'threads_' + url.replace('https://', '').replace('/', '').replace('.', '_') +'.html'
            with open('Files03/' + filename, 'w', encoding='utf-8') as f:
                f.write(text)
    # print(f'Downloaded {url} in {time.time() - start_time:.2f} seconds')

# start_time = time.time()

start_time = time.time()

async def main():
    tasks = [asyncio.ensure_future(get_urls(url)) for url in urls]
    await asyncio.gather(*tasks)



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

print(f'Time {time.time() - start_time}')