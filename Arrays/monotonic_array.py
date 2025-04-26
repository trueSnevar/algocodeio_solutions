"""
Монотонный массив

легко
решено

Дан целочисленный массив nums. Нужно вернуть true, если массив монотонный, и false в обратном случае.
Массив считается монотонным, если он отсортирован (по возрастанию или убыванию).

Пример 1:

Ввод: nums = [1,2,2,2,3]
Вывод: true

Пример 2:

Ввод: nums = [5,4,-10]
Вывод: true

"""
from typing import *

def is_monotonic(nums: List[int]) -> bool:
    # идея в том, что нам не важно монотонно возрастает массив
    # или монотонно убыват, поэтому мы заводим 2 флага:
    # на монотонное возрастание и на монотонное убывание
    is_inc = True
    is_dec = True
    for i in range(1, len(nums)):
        is_inc = is_inc and nums[i - 1] <= nums[i]
        is_dec = is_dec and nums[i - 1] >= nums[i]
    return is_inc or is_dec


if __name__ == "__main__":
    ex1 = [1,2,2,2,3]
    ex2 = [5,4,-10]

    ans1 = is_monotonic(ex1)
    ans2 = is_monotonic(ex2)
    print(ans1)
    print(ans2)

"""
Оценка сложности

Время: O(n), где n - длина массива nums
Память: O(1)
"""