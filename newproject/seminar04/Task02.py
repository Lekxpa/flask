# Написать программу, которая считывает список из 10 URL-адресов
# и одновременно загружает данные с каждого адреса.
# После загрузки данных нужно записать их в отдельные файлы.
# Используйте процессы.

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
start_time = time.time()
def get_urls(url):
    response = requests.get(url)
    filename = 'threads_' + url.replace('https://', '').replace('/', '').replace('.', '_') +'.html'
    with open('Files/' + filename, 'w', encoding='utf-8') as f:
        f.write(response.text)
    print(f'Downloaded {url} in {time.time() - start_time:.2f} seconds')

# start_time = time.time()
processes = []

if __name__ == '__main__':

    for url in urls:
        process = Process(target=get_urls, args=(url, ))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    # print(f'Time {time.time() - start_time}')