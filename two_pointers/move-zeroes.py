"""
Перемещение нулей

легко
решено

Дан массив nums. Нужно переместить все нули (0) в конец массива,
при этом порядок остальных элементов должен сохраниться.

Необходимо изменять исходный массив напрямую,
без создания нового массива для хранения результата.

Пример 1:

Ввод: nums = [2,1,0,0,4,0,9]
Вывод: [2,1,4,9,0,0,0]

Пример 2:

Ввод: nums = [0]
Вывод: [0]

Ограничения:
- len(nums) ≥ 1
"""
from typing import List


def move_zeroes(nums: List[int]) -> List[int]:
    """
    Перемещает все нули в конец списка nums, сохраняя порядок остальных элементов.
    Изменяет массив на месте.
    """
    # указывает на какую позицию поставим следующий элемент не равный 0
    nxt_non_zero = 0
    # указывает на следующий не нулевой элемент
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[nxt_non_zero], nums[i] = nums[i], nums[nxt_non_zero]
            nxt_non_zero += 1
    return nums


if __name__ == "__main__":
    # Пример 1
    nums1 = [2, 1, 0, 0, 4, 0, 9]
    move_zeroes(nums1)
    print(nums1)  # [2,1,4,9,0,0,0]

    # Пример 2
    nums2 = [0]
    move_zeroes(nums2)
    print(nums2)  # [0]

# Оценка сложности:
# Время: O(n), где n = len(nums)
# Память: O(1) дополнительной памяти
