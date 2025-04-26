"""
Максимальное произведение
легко
решено

Дан массив nums, состоящий из положительных целых чисел.
Нужно вернуть максимальное произведение двух различных элементов массива.

Пример 1:

Ввод: nums = [5,3,10,2,8,5]
Вывод: 80
Объяснение: 10 * 8 = 80

Пример 2:

Ввод: nums = [10,10,10]
Вывод: 100

"""

from typing import *

def max_product(nums: List[int]) -> int:
    a = 0
    b = 0

    for num in nums:
        if num > a:
            b = a
            a = num
        elif num > b:
            b = num

    return a * b

if __name__ == "__main__":
    ex1 = [5,3,10,2,8,5]
    ex2 = [10,10,10]

    ans1 = max_product(ex1)
    ans2 = max_product(ex2)
    print(ans1)
    print(ans2)

"""
Оценка сложности

Время: O(n), где n - длина массива nums
Память: O(1)
"""