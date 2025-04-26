"""
Подмассив с суммой K

средне
решено

Дан массив nums и число k. Нужно найти количество подмассивов, где сумма всех элементов равна числу k.

Подмассив — это непрерывная непустая последовательность элементов внутри массива.

Пример 1:

Ввод: nums = [7,3,1,5,5,5,10], k = 10
Вывод: 4
Объяснение: [7,3], [5,5], [5,5], [10]

Пример 2:

Ввод: nums = [-100,1,1,1,1,1,3,2,2], k = 4
Вывод: 4
Объяснение: [1,1,1,1], [1,1,1,1], [1,3], [2,2]

Ограничения:

len(nums) >= 1

"""

from typing import *


def count_subarrays(nums: List[int], target_sum: int) -> int:
    # ключ - префиксная сумма, значение - сколько раз встретили
    prefix_sums = {0: 1}

    # текущая префиксная сумма
    current_prefix_sum = 0

    count = 0
    for el in nums:
        current_prefix_sum += el

        # проверяем встречали ли мы уже префиксный массив
        # с суммой current_prefix_sum - target_sum
        if (current_prefix_sum - target_sum) in prefix_sums:
            # если встречали - то к ответу прибавлем
            # число сколько раз уже встретили
            count += prefix_sums[current_prefix_sum - target_sum]

        # добавляем текущую префиксную сумму в массив
        prefix_sums[current_prefix_sum] = 1 + prefix_sums.get(current_prefix_sum, 0)
    return count


if __name__ == "__main__":
    ex1 = [7,3,1,5,5,5,10]
    k1 = 10

    ex2 = [-100,1,1,1,1,1,3,2,2]
    k2 = 4

    ans1 = count_subarrays(ex1, k1)
    ans2 = count_subarrays(ex2, k2)
    print(ans1)
    print(ans2)

"""
Оценка сложности

Время: O(n), где n - длина массива nums
Память: O(n), где n - длина массива nums
"""