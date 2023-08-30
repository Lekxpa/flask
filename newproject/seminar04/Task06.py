# Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск. Каждое изображение должно сохраняться в отдельном файле, название которого соответствует названию изображения в URL-адресе.
# Например URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# - Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
# - Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
# - Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени выполнения программы.



import threading
import requests
import time

urls = [
    'https://www.nan-news.ru/wp-content/uploads/2020/05/nigel-tadyanehondo-230499-1-1-scaled.jpg',
    'https://img-cdn.herbeauty.co/wp-content/uploads/2019/03/12_Things_No_Woman_Should_Have_To_Apologize_For6.jpg',
    'https://i.pinimg.com/originals/76/db/3d/76db3dc1120aa3a65f808365213ca850.jpg',
    'https://i.pinimg.com/originals/3a/f7/98/3af798e32c844260b1436ff32c869361.jpg',
    ]

def get_urls(url):
    response = requests.get(url)
    filename = 'threads_' + url.replace('https://', '').replace('/', '').replace('.', '_') +'.jpg'
    with open('Files06/' + filename, 'wb') as f:
        f.write(response.content)

start_time = time.time()
threads = []

for u in urls:
    t = threading.Thread(target=get_urls, args=[u])
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f'Time {time.time() - start_time}')