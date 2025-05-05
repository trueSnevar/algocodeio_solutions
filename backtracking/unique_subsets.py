"""
Уникальные подмножества

средне
решено

Дан массив уникальных целых чисел nums. Нужно найти все возможные наборы чисел,
которые можно из него составить (включая пустой набор и сам массив).

Порядок чисел в наборах не имеет значения, и одинаковых наборов быть не должно.

Пример 1:

Ввод: nums = [3,6,17]
Вывод: [[],[3],[6],[3,6],[17],[3,17],[6,17],[3,6,17]]

Пример 2:

Ввод: nums = [11]
Вывод: [[],[11]]

Ограничения:

len(nums) >= 1
"""

from typing import *


def generate_subsets(nums: List[int]) -> List[List[int]]:
    ans = []
    n = len(nums)
    def backtrack(idx: int, subset: List[int]):
        if idx == n:
            ans.append(subset[:])
            return

        # не берем следующий элемент
        backtrack(idx + 1, subset)

        # берем следующий элемент
        subset.append(nums[idx])
        backtrack(idx + 1, subset)
        subset.pop()

    backtrack(0, [])
    return ans

if __name__ == "__main__":
    ex1 = [3,6,17]
    ex2 = [11]

    ans1 = generate_subsets(ex1)
    ans2 = generate_subsets(ex2)

    print(ans1)
    print(ans2)



"""
Оценка сложности

Время: O(n * 2ⁿ), где n — это размер массива nums
Память: O(n * 2ⁿ), где n — это размер массива nums
"""
