# Задание №7
# � Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# � Массив должен быть заполнен случайными целыми числами от 1 до 100.
# � При решении задачи нужно использовать асинхронность.
# � В каждом решении нужно вывести время выполнения  вычислений.
import asyncio
from random import randint
import time


arr = [randint(1, 100) for _ in range(1000000)]
start_time = time.time()


async def sum_elem_arr(arr):
    result = 0
    for i in arr:
        result += i
    print(f'Сумма: {result}')
    return result


list_t = [arr[i:i + 1000000] for i in range(1, 1000000, 1000000)]


async def main(list_t):
    lst = []
    for i in list_t:
        task = asyncio.create_task(sum_elem_arr(i))
        lst.append(task)
    res_t = await asyncio.gather(*lst)
    print(f'Сумма элементов массива: {sum (res_t)}')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(list_t))

print(f'Время выполнения: {time.time() - start_time:.5f} sec')