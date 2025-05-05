"""
Перестановки

средне
решено

Дан массив nums, содержащий различные целые числа.
Необходимо вернуть все возможные перестановки элементов этого массива.
Порядок вывода перестановок может быть любым.

Пример 1:

Ввод: nums = [3,6,9]
Вывод: [[3,6,9],[3,9,6],[6,3,9],[6,9,3],[9,3,6],[9,6,3]]

Пример 2:

Ввод: nums = [0,9]
Вывод: [[0,9],[9,0]]

Пример 3:

Ввод: nums = [0]
Вывод: [[0]]
Ограничения:

len(nums) >= 1
"""

from typing import *


def permutations(nums: List[int]) -> List[List[int]]:
    res = []
    n = len(nums)
    used = [False] * n

    def backtrack(subset: List[int]):
        if len(subset) == n:
            res.append(subset[:])
            return

        for i in range(n):
            if used[i]:
                continue
            used[i] = True

            subset.append(nums[i])
            backtrack(subset)
            subset.pop()

            used[i] = False

    backtrack([])
    return res

if __name__ == "__main__":
    ex1 = [3,6,9]
    ex2 = [0,9]
    ex3 = [0]

    ans1 = permutations(ex1)
    ans2 = permutations(ex2)
    ans3 = permutations(ex3)

    print(ans1)
    print(ans2)
    print(ans3)



"""
Время: O(n * n!), где n количество элементов в массиве nums
Память: O(n * n!), где n количество элементов в массиве nums
"""
