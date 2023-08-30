# Задание №7
# � Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# � Массив должен быть заполнен случайными целыми числами от 1 до 100.
# � При решении задачи нужно использовать многопоточность,
# � В каждом решении нужно вывести время выполнения  вычислений.


import threading
import time
from random import randint

arr = [randint(1, 100) for _ in range(1000000)]
start_time = time.time()
result = 0


def sum_elem_arr(arr):
    global result
    for i in arr:
        result += i
    print(f'Сумма: {result}')


list_t = [arr[i:i + 1000000] for i in range(1, 1000000, 1000000)]

threads = []
for l in list_t:
    t = threading.Thread(target=sum_elem_arr, args=[l])
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f'Время выполнения: {time.time() - start_time:.5f} sec.')