"""
Сортировка элементов в квадрате

легко
решено

Дан массив nums, отсортированный в неубывающем порядке. Нужно вернуть
отсортированный массив, состоящий из всех элементов nums, возведенных в квадрат.

Неубывающий порядок – каждый следующий элемент ≥ предыдущего.

Пример 1:

Ввод: nums = [-3,-2,0,1,3,5]
Вывод: [0,1,4,9,9,25]

Пример 2:

Ввод: nums = [-5,-3,-1]
Вывод: [1,9,25]

Ограничения:
- len(nums) ≥ 1
"""
from typing import List


def sorted_squares(nums: List[int]) -> List[int]:
    """
    Возвращает новый массив, содержащий квадраты элементов nums,
    отсортированные по неубывающему порядку.
    Используется метод двух указателей с O(n) временем.
    """
    n = len(nums)
    result = []
    left, right = 0, n - 1

    # Сравниваем по абсолютному значению и заполняем result с конца
    while left <= right:
        left_sq = nums[left] * nums[left]
        right_sq = nums[right] * nums[right]
        if left_sq > right_sq:
            result.append(left_sq)
            left += 1
        else:
            result.append(right_sq)
            right -= 1

    return list(reversed(result))


if __name__ == "__main__":
    # Пример 1
    print(sorted_squares([-3, -2, 0, 1, 3, 5]))  # [0,1,4,9,9,25]
    # Пример 2
    print(sorted_squares([-5, -3, -1]))          # [1,9,25]

# Оценка сложности:
# Время: O(n), где n = len(nums)
# Память: O(n) на выходной массив
