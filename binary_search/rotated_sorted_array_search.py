"""
Поиск в сдвинутом массиве

средне
решено

Дано число target и массив уникальных чисел nums, который изначально был отсортирован по возрастанию,
а затем несколько раз последний элемент переместили в начало.
Количество таких операций неизвестно и не является входным параметром.

Найдите индекс числа target в массиве или верните -1, если такого числа нет.

Пример 1:

Ввод: nums = [4,8,9,1,2], target = 9
Вывод: 2

Пример 2:

Ввод: nums = [1,2,3,4,5], target = 5
Вывод: 4

Пример 3:

Ввод: nums = [3, 1], target = 3
Вывод: 0

Ограничения:

len(nums) >= 1

"""

from typing import *

def find_offset(nums: List[int]):
    l, r = -1, len(nums) - 1
    last_val = nums[-1]
    while r - l > 1:
        m = (l + r) // 2
        #  good        bad
        # [4 5 6 7  |  0 1 2]
        #        l     r
        if nums[m] > last_val:
            l = m
        else:
            r = m
    return r

def search(nums: List[int], target: int) -> int:
    # обычный бинарный поиск, но смещаем на offset дополнительно
    offset = find_offset(nums)
    l, r = offset, len(nums) + offset
    while r - l > 1:
        m = (l + r) // 2
        if nums[m % len(nums)] <= target:
            l = m
        else:
            r = m
    real_left = l % len(nums)

    return real_left if nums[real_left] == target else -1

if __name__ == "__main__":
    ex1 = [4,8,9,1,2]
    target1 = 9

    ex2 = [1,2,3,4,5]
    target2 = 5

    ex3 = [3, 1]
    target3 = 3

    ans1 = search(ex1, target1)
    ans2 = search(ex2, target2)
    ans3 = search(ex3, target3)
    print(ans1)
    print(ans2)
    print(ans3)


"""
Оценка сложности

Время: O(log(n)), где n - длина массива nums
Память: O(1)
"""